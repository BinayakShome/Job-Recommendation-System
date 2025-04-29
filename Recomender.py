import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load dataset
df = pd.read_csv("jobs.csv")

# Step 2: Fill missing values
df['skills'] = df['skills'].fillna("")

# Step 3: TF-IDF Vectorization on skills
vectorizer = TfidfVectorizer()
skill_matrix = vectorizer.fit_transform(df['skills'])

# Step 4: Function to recommend jobs
def recommend_jobs(user_skills, top_n=3):
    user_skills = [user_skills]
    user_vec = vectorizer.transform(user_skills)
    similarity = cosine_similarity(user_vec, skill_matrix).flatten()
    
    indices = similarity.argsort()[::-1][:top_n]
    recommended_jobs = df.iloc[indices]

    print("\nTop Job Recommendations:\n")
    for _, row in recommended_jobs.iterrows():
        print(f"Title: {row['title']} | Skills: {row['skills']} | Experience: {row['experience']}")
    print()

# === Example usage ===
if __name__ == "__main__":
    print("Enter your skills (comma-separated):")
    user_input = input("> ")
    recommend_jobs(user_input)