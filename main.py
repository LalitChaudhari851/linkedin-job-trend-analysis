
from scraper import get_job_postings
from analyzer import analyze_jobs
import pandas as pd
import json
import os

if __name__ == "__main__":
    roles = ['data analyst', 'software engineer']
    cities = ['Pune', 'Mumbai']
    all_jobs = []

    for role in roles:
        for city in cities:
            print(f"Fetching jobs for role '{role}' in city '{city}'...")
            jobs = get_job_postings(role, city, pages=1)
            all_jobs.extend(jobs)

    df, top_skills_by_city, skill_matrix = analyze_jobs(all_jobs)

    if not df.empty:
        print("\n✅ Job data fetched and analyzed!")
        print(df.head())

        # Ensure frontend/data folder exists
        os.makedirs("../frontend/data", exist_ok=True)

        # Export results to JSON for frontend use
        top_skills_by_city.to_json("../frontend/data/top_skills_by_city.json", orient='records')
        skill_matrix.to_json("../frontend/data/skill_vs_role.json", orient='index')

        print("\n📁 JSON files saved in frontend/data/")
    else:
        print("\n⚠ No data to process.")
