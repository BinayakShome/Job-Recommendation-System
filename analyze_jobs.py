import pandas as pd

# Load the data
df = pd.read_csv('live_job_data.csv')

# See first few entries
print(df.head())

# See available columns
print("\nColumns:", df.columns.tolist())

# Check for any missing data
print("\nMissing values:\n", df.isnull().sum())