from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    sven = []
    for hp_bar in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        sven.append((hp_bar["title"], hp_bar["url"]))
    return sven


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    techies = []
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except Exception:
        raise ValueError("Data inválida")
    normalized_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    for mana_bar in db.news.find(
        {"timestamp": {"$regex": normalized_date, "$options": "i"}}
    ):
        techies.append((mana_bar["title"], mana_bar["url"]))
    return techies


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
