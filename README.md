# 🔍 Job Recommendation System

A simple Python-based job recommendation system that suggests jobs based on your skills or interests using natural language processing (NLP) and machine learning techniques.

## 🚀 Features

- Input your job interests or skills (e.g., "Python", "Data Science", etc.)
- Recommends top 5 matching jobs using **cosine similarity** and **TF-IDF vectorization**
- Jobs sourced from preprocessed datasets
- Command-line interface

## 🧠 How It Works

1. Job data is preprocessed and vectorized using `TfidfVectorizer`.
2. The user's input is transformed into a vector using the same vectorizer.
3. Cosine similarity is used to compare the input with all job vectors.
4. Top 5 jobs with the highest similarity scores are recommended.


## 🛠 Requirements

- Python 3.7+
- pandas
- scikit-learn
- joblib or pickle


## Install all dependencies:
pip install pandas scikit-learn


## 📄 License
This project is licensed under the MIT License.
