from tech_news.database import search_news
from datetime import datetime


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
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        filter_date = []

        for infoDate in search_news(
            {"timestamp": {"$regex": date_format}}
        ):
            filter_date.append(
                (infoDate["title"], infoDate["url"])
            )

        return filter_date
    except ValueError:
        raise ValueError("Data inválida")


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
