import pandas as pd
from skills import extract_skills

def analyze_jobs(jobs):
    df = pd.DataFrame(jobs)
    df['skills'] = df['summary'].apply(extract_skills)
    df_exploded = df.explode('skills')

    top_skills_by_city = df_exploded.groupby(['city', 'skills']).size().reset_index(name='count')
    skill_matrix = df_exploded.pivot_table(index='skills', columns='role', aggfunc='size', fill_value=0)

    return df, top_skills_by_city, skill_matrix