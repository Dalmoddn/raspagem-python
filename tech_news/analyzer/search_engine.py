from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    sven = []
    for bar in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        sven.append((bar["title"], bar["url"]))
    return sven


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
