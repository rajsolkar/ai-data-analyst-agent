# AI Data Analyst Agent

An intelligent AI-powered Data Analyst Agent that automates the entire analytics workflow, from data collection, cleaning, and analysis to generating interactive dashboards using Streamlit.

---

## Overview
This personal project aims to replicate the work of a human data analyst. It connects to a local SQLite database, accepts natural language queries, and uses AI to generate SQL, execute it safely, and visualize results.

---

## Tech Stack
- Python 3.13
- SQLite (for local data storage)
- OpenAI API / Ollama (for AI text-to-SQL intelligence)
- Streamlit (for frontend dashboard)
- Pandas (for data manipulation)

---

## Features
- AI-generated SQL queries from plain English prompts  
- Secure database querying (sandboxed)  
- Automatic data analysis and summaries  
- Streamlit dashboard for visual exploration  
- Easy to extend with your own datasets  

---

## Folder Structure
ai-data-analyst-agent/
│
├── app.py # Streamlit main app
├── db/
│ └── data.db # SQLite database
├── utils/
│ ├── ai.py # AI interaction logic
│ └── data.py # Data cleaning and querying
└── libraries.txt # List of Python dependencies

---

## Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/rajsolkar/ai-data-analyst-agent.git
cd ai-data-analyst-agent
```
### 2. Create a virtual environment (optional)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```
### 3. Install dependencies
```bash
pip install -r libraries.txt
```
### 4. Run the app
```bash
streamlit run app.py
```

## Future Improvements
- Add multi-database support (PostgreSQL, MySQL)
- Integrate real-time data pipelines
- Add user authentication and access control
- Deploy publicly using Streamlit Cloud or Hugging Face Spaces

⚠️ **Note:**  
The OpenAI API key used in this demo has limited credits, so you may occasionally see an "insufficient_quota" error.  
The full logic and LLM integration work correctly when used with an active API key.

## Author
Raj Solkar  
Aspiring Data Analyst | AI Enthusiast  
rajsolkar26@gmail.com  
Linked in : https://www.linkedin.com/in/raj-solkar-26032006m/
Github Profile : https://github.com/rajsolkar