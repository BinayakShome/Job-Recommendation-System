import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load data and models
df = pd.read_csv('preprocessed_jobs.csv')
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('job_vectors.pkl', 'rb') as f:
    job_vectors = pickle.load(f)

# Ask user for input (skills, interests, etc.)
user_input = input("Enter your skills or job interest: ")

# Transform user input into vector
user_vector = vectorizer.transform([user_input])

# Compute cosine similarity
similarities = cosine_similarity(user_vector, job_vectors).flatten()

# Get top 5 most similar jobs
top_indices = similarities.argsort()[-5:][::-1]

# Show recommendations
print("\n📢 Top 5 Job Recommendations:\n")
for idx in top_indices:
    print(f"Title   : {df['title'][idx]}")
    print(f"Company : {df['company'][idx]}")
    print(f"Location: {df['location'][idx]}")
    print(f"Desc    : {df['description'][idx][:150]}...\n")