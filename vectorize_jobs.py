import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load cleaned data
df = pd.read_csv('preprocessed_jobs.csv')

# Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)  # You can increase/decrease based on data size
vectors = vectorizer.fit_transform(df['cleaned_text'])

# Save the vectorizer and vectors
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('job_vectors.pkl', 'wb') as f:
    pickle.dump(vectors, f)

print("✅ TF-IDF vectors and vectorizer saved!")