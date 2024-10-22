from time import sleep
import requests
from parsel import Selector
from tech_news.database import create_news


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
    qop = {}
    selector = Selector(text=html_content)
    qop["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    qop["title"] = selector.css(".entry-title::text").get().strip()
    qop["timestamp"] = selector.css(".meta-date::text").get()
    qop["writer"] = selector.css(".author a::text").get()
    qop["reading_time"] = int(
        selector.css(".meta-reading-time::text").get().split()[0]
    )
    qop["summary"] = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    qop["category"] = selector.css(".category-style .label::text").get()
    return qop


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    link = "https://blog.betrybe.com"
    news_list = []
    while len(news_list) < amount and link:
        news = fetch(link)
        if not news:
            break
        links = scrape_updates(news)
        for news_link in links:
            news_html = fetch(news_link)
            if news_html:
                news_list.append(scrape_news(news_html))
        link = scrape_next_page_link(news)
    resulting_news = news_list[:amount]
    create_news(resulting_news)
    return resulting_news
