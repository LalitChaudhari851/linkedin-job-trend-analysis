import re

COMMON_SKILLS = ['python', 'sql', 'excel', 'tableau', 'java', 'c++', 'aws', 'power bi', 'communication', 'machine learning']

def extract_skills(text):
    found = []
    text = text.lower()
    for skill in COMMON_SKILLS:
        if re.search(rf'\b{re.escape(skill)}\b', text):
            found.append(skill)
    return found