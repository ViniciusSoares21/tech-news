import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news


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
    soup = BeautifulSoup(html_content, "html.parser")
    news = {}
    news["url"] = soup.find(
        "link",
        {"rel": "canonical"},
    )["href"]
    news["title"] = soup.find("h1", {"class": "entry-title"}).string.strip()
    news["timestamp"] = soup.find("li", {"class": "meta-date"}).string
    news["writer"] = soup.find("li", {"class": "meta-author"}).a.string
    news["reading_time"] = int(
        soup.find("li", {"class": "meta-reading-time"}).text.split()[0]
    )
    news["summary"] = soup.find(
        "div", {"class": "entry-content"}
    ).p.text.strip()
    news["category"] = soup.find("span", {"class": "label"}).string
    return news


# Requisito 5
def get_tech_news(amount):
    news = []
    url_page = 'https://blog.betrybe.com/'
    while len(news) < amount:
        main_page = fetch(url_page)
        list_urls = scrape_updates(main_page)
        for url in list_urls:
            if len(news) == amount:
                break
            content_page = fetch(url)
            obj_news = scrape_news(content_page)
            news.append(obj_news)
        url_page = scrape_next_page_link(main_page)
    create_news(news)
    return news
