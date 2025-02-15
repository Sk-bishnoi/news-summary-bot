
import requests
import pandas as pd
from datetime import datetime, timedelta
from src.python.app.constant.constants import NEWS_API_KEY, NEWS_API_URL, CATEGORIES
from src.python.app.common.model import summarize_text

def fetch_news(category, start_date, end_date):
    """Fetch news from API based on category and date range."""
    url = f"{NEWS_API_URL}?q={CATEGORIES[category]}&from={start_date}&to={end_date}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [{"title": a["title"], "summary": summarize_text(a["description"])} for a in articles]
    return []

def get_last_n_days(n=5):
    """Return start and end dates for the last N days."""
    end_date = datetime.today()
    start_date = end_date - timedelta(days=n)
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')
