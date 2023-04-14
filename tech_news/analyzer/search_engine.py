from tech_news.database import get_collection
import re


# Requisito 7
def search_by_title(title: str):
    result = get_collection().find(
        {"title": re.compile(title, re.IGNORECASE)},
        {"_id": False, "title": True, "url": True},
    )

    return [(item["title"], item["url"]) for item in result]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
