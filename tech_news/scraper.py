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
    next_page = Selector(html_content)
    link = next_page.css("a.next::attr(href)").get()
    return link
    # https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/7e82ac53-a588-412b-95a5-19727d70ed3a/day/9488d307-4a72-4c82-887f-d860ad20a1af/lesson/e9c42a21-2d88-4ef0-b3c9-f60e8f81235a


# Requisito 4
def scrape_news(html_content):
    news = Selector(text=html_content)
    title = news.css("h1::text").get()
    url = news.css("link[rel=canonical]::attr(href)").get()
    timestamp = news.css("li.meta-date::text").get()
    writer = news.css("span.author a::text").get()
    reading_time = news.css("li.meta-reading-time::text").get()
    summary = news.css("div.entry-content > p:first-of-type *::text").getall()
    category = news.css("span.label::text").get()

    result = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time.split(' ')[0]),
        "summary": "".join(summary).strip(),
        "category": category,
    }

    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
