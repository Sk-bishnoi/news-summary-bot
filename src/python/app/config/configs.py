

import os

class Config:
    API_KEY = os.getenv("NEWS_API_KEY", "YOUR_NEWS_API_KEY")
    BASE_URL = "https://newsapi.org/v2/everything"
    DEFAULT_DAYS = 5  # Show last 5 days by default

config = Config()
