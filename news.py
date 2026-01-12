import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

URL = "https://newsapi.org/v2/top-headlines"
PARAMS = {
    "language": "en",
    "pageSize": 5,
    "apiKey": NEWS_API_KEY
}

def get_news():
    res = requests.get(URL, params=PARAMS)
    data = res.json()
    articles = []

    if "articles" in data:
        for a in data["articles"]:
            articles.append({
                "title": a.get("title", ""),
                "description": a.get("description", "")
            })
    return articles
