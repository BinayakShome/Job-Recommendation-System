import requests
import pandas as pd

# Replace with your keys
APP_ID = "8cd905d0"
APP_KEY = "96378bf90b7ab21fee803adae8201981"

# Base URL
url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

# Query parameters
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 10,
    "what": "python developer",
    "content-type": "application/json"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    jobs = response.json()["results"]
    job_data = []

    for job in jobs:
        job_data.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "created": job.get("created"),
            "category": job.get("category", {}).get("label")
        })

    df = pd.DataFrame(job_data)
    df.to_csv("live_job_data.csv", index=False)
    print("✅ Job data saved to live_job_data.csv")
else:
    print("❌ Failed to fetch jobs:", response.status_code)