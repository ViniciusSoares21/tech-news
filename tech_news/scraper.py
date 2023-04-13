import requests
import time
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    try:
        res = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        if res.status_code != 200:
            raise ValueError

        return res.text
    except (requests.ReadTimeout, ValueError):
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    links = soup.find_all("a", {"class": "cs-overlay-link"})
    href = []
    for link in links:
        href.append(link.get("href"))
    return href


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.find(
            "a",
            {"class": "next page-numbers"},
        )["href"]
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
