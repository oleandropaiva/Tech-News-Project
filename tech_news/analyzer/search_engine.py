from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    searchNews = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )

    result = []
    for infos in searchNews:
        result.append(
            (infos["title"], infos["url"])
        )
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    search_category = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    result = []
    for infos in search_category:
        result.append(
            (infos["title"], infos["url"])
        )
    return result
