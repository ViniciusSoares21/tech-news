from tech_news.database import get_collection
import re
import datetime


# Requisito 7
def search_by_title(title: str):
    result = get_collection().find(
        {"title": re.compile(title, re.IGNORECASE)},
        {"_id": False, "title": True, "url": True},
    )

    return [(item["title"], item["url"]) for item in result]


# Requisito 8
def search_by_date(date):
    try:
        date_covert = datetime.date.fromisoformat(date).strftime("%d/%m/%Y")
        result = get_collection().find(
            {"timestamp": date_covert},
            {"_id": False, "title": True, "url": True},
        )

        return [(item["title"], item["url"]) for item in result]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
