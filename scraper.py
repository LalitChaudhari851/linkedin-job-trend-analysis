import requests
from bs4 import BeautifulSoup
import time

def get_job_postings(role, city, pages=1):
    jobs = []
    role_query = role.replace(' ', '+')
    city_query = city.replace(' ', '+')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    for page in range(pages):
        url = f"https://www.indeed.com/jobs?q={role_query}&l={city_query}&start={page*10}"

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch page {page + 1} for {role} in {city}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        cards = soup.find_all('div', class_='job_seen_beacon')
        if not cards:
            print(f"No job cards found on page {page + 1} for {role} in {city}")
            continue

        for card in cards:
            title = card.find('h2', class_='jobTitle')
            summary = card.find('div', class_='job-snippet')

            jobs.append({
                'title': title.text.strip() if title else '',
                'summary': summary.text.strip().replace("\\n", " ") if summary else '',
                'city': city,
                'role': role
            })

        time.sleep(2)  # increased delay to be polite

    return jobs
