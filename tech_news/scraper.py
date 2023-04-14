import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url: str):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        response.raise_for_status()
        return response.text
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.Timeout
    ):
        return None


# Requisito 2
def scrape_updates(html_content):
    update = Selector(html_content)
    news_link = update.css("div.cs-overlay a::attr(href)").getall()
    return news_link

    # response = requests.get('https://blog.betrybe.com/')
    # selector = Selector(response.text)
    # print(selector.css("div.cs-overlay a::attr(href)").get())
    # referencia raspagem de dados/analisando respostas (course)


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
