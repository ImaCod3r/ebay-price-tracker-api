from bs4 import BeautifulSoup
from utils import *
import logging
import requests

CONFIGS = {
    "url": "https://www.ebay.com/sch/",
    "headers": { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" }
}

def make_request(configs, query):
    url = configs["url"] + query
    headers = configs["headers"]
    
    try: 
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logging.error(f"Error when making the request: {e}")
        return None

def scrap_page(html):
    soup = BeautifulSoup(html, "html.parser")
    
    titles = soup.select(".s-item__wrapper .s-item__title")
    prices = soup.select(".s-item__wrapper .s-item__price")
    links = soup.select(".s-item__wrapper .s-item__link")
    
    return {
        "titles": [title.get_text(strip=True) for title in titles],
        "prices": [price.get_text(strip=True) for price in prices],
        "links": [link.get("href") for link in links]
    }

def handle_data_from_page(items):
    numeric_prices = [getNumericPrice(price) for price in items["prices"]]
    average_price = getAveragePrice(numeric_prices)
    
    below_average_items = [
        {
            "title": items["titles"][index],
            "price": items["prices"][index],
            "link": items["links"][index]
        }
        for index in range(len(items["titles"])) if numeric_prices[index] <= average_price
    ]
    
    
    return {
        "total": len(items["titles"]),
        "average price": average_price,
        "cheaper": below_average_items
    }
    
def get_data(query):
    html = make_request(CONFIGS, query)
    if html is None:
        return False

    items = scrap_page(html)
    return handle_data_from_page(items)