import pandas as pd
import re

# Load the data
df = pd.read_csv('live_job_data.csv')

# Combine 'title' and 'description'
df['text'] = df['title'] + ' ' + df['description']

# Preprocessing function
def clean_text(text):
    text = text.lower()                              # Lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)        # Remove special characters
    text = re.sub(r'\s+', ' ', text)                  # Remove extra spaces
    return text

# Apply cleaning
df['cleaned_text'] = df['text'].apply(clean_text)

# Save preprocessed data
df[['cleaned_text']].to_csv('preprocessed_jobs.csv', index=False)

print("✅ Preprocessing done and saved as preprocessed_jobs.csv")