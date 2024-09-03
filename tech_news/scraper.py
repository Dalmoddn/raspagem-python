from time import sleep
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        html_content = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if html_content.status_code == 200:
            return html_content.text
        return None
    except requests.exceptions.RequestException:
        return None
    finally:
        sleep(1)


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    list_updates = []
    picker = Selector(text=html_content)
    for news in picker.css(".cs-overlay"):
        list_updates.append(news.css("a::attr(href)").get())
    return list_updates


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    return Selector(text=html_content).css(".next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
