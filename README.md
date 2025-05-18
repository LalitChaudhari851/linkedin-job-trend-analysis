# 🔍 LinkedIn Job Trend Analysis (Web Scraping Project)

A complete Python + Web App project that scrapes job listings from Indeed (inspired by LinkedIn trends) to analyze **in-demand skills across cities and roles**. Displays the results in an interactive web dashboard.

---

## 🎯 Objectives

- Scrape job listings using Python and BeautifulSoup
- Extract job titles, skill keywords, and city names
- Analyze skill demand across roles and locations
- Display interactive tables and charts on a modern web dashboard

---

## 🛠️ Tools & Technologies

| Backend | Frontend |
|--------|----------|
| Python (requests, BeautifulSoup, pandas) | HTML, CSS, JavaScript |
| Excel (optional export) | JSON (data from backend) |

---

## 🚀 How to Run the Project

### 📥 1. Clone or Download

```bash
git clone https://github.com/your-username/linkedin-job-trend-analysis.git
cd linkedin-job-trend-analysis
```

### 📦 2. Install Python Requirements

```bash
cd backend
pip install -r requirements.txt
# Or install manually:
# pip install requests beautifulsoup4 pandas openpyxl
```

### ⚙ 3. Run the Scraper + Analyzer

```bash
python main.py
```

This will:
- Scrape job postings from Indeed.com
- Extract skill trends
- Save JSON files in `frontend/data/`

### 🌐 4. Launch the Dashboard

```bash
cd ../frontend
# Open index.html in your browser
```

---

## 📊 Example Outputs

- ✅ JSON files:
  - `top_skills_by_city.json`
  - `skill_vs_role.json`
- 📈 Visuals ready for enhancement with Chart.js or D3.js
- 💼 Ready for deployment or portfolio use

---

## 📌 Project Structure

```
linkedin-job-trend-analysis/
│
├── backend/
│   ├── main.py
│   ├── scraper.py
│   ├── analyzer.py
│   ├── skills.py
│   └── README.md
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── data/
│       ├── top_skills_by_city.json
│       └── skill_vs_role.json
│
└── README.md
```

---

## 🧑‍💻 Author

**Lalit Chaudhari**  
_Python Developer & Data Analyst_  
[GitHub](https://github.com/your-username) | [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📝 License

This project is open-source and free to use under the [MIT License](LICENSE).
