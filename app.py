from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load your dataset
df = pd.read_csv('job_data.csv')

# TF-IDF Vectorizer (improved with n-gram)
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
skill_matrix = vectorizer.fit_transform(df['skills'])

def recommend_jobs(user_skills, user_experience=0, top_n=3):
    user_skills = [user_skills]
    user_vec = vectorizer.transform(user_skills)
    similarity = cosine_similarity(user_vec, skill_matrix).flatten()

    df['similarity'] = similarity

    # Filter experience
    filtered_df = df.copy()

    def experience_filter(exp, user_exp):
        try:
            if "year" in exp.lower():
                num = int(''.join([c for c in exp if c.isdigit()]))
                return num <= user_exp + 2
            else:
                return True
        except:
            return True

    filtered_df = filtered_df[filtered_df['experience'].apply(lambda x: experience_filter(x, user_experience))]

    # Sort and select
    filtered_df = filtered_df.sort_values(by='similarity', ascending=False)
    recommended_jobs = filtered_df.head(top_n)

    recommendations = []
    for _, row in recommended_jobs.iterrows():
        recommendations.append({
            "title": row['title'],
            "skills": row['skills'],
            "experience": row['experience']
        })
    return recommendations

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_skills = data.get('skills', '')
    user_experience = data.get('experience', 0)
    top_n = data.get('top_n', 3)

    if not user_skills:
        return jsonify({"error": "Skills not provided"}), 400

    results = recommend_jobs(user_skills, user_experience, top_n)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)