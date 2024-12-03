from bs4 import BeautifulSoup
from utils import *
import requests

configs = {
    "url": "https://www.ebay.com/sch/",
    "headers": { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" }
}

def makeRequest(configs, query):
    query = formatText(query)
    url = configs["url"] + query
    headers = configs["headers"]
    
    response = requests.get(url, headers=headers)
    html = response.content
    
    return html

def scrapPage(html):
    soup = BeautifulSoup(html, "html.parser")
    
    titles = soup.select(".s-item__wrapper .s-item__title")
    prices = soup.select(".s-item__wrapper .s-item__price")
    links = soup.select(".s-item__wrapper .s-item__link")
    
    items = {
        "titles": [title.text for title in titles],
        "prices": [price.text for price in prices],
        "links": [link.get("href") for link in links]
    }
    
    return items

def handleDataFromPage(items):
    numeric_prices = [getNumericPrice(price) for price in items["prices"]]
    average_price = getAveragePrice(numeric_prices)
    
    below_average_items = []
    for index in range(len(items["titles"])):
        if numeric_prices[index] <= average_price:
            below_average_items.append({
                "title": items["titles"][index],
                "price": items["prices"][index],
                "link": items["links"][index]
            })
    
    return {
        "total": len(items["titles"]),
        "average price": average_price,
        "cheaper": below_average_items
    }
    
def getData(query):
    try:
        html = makeRequest(configs, query)
        soup = scrapPage(html)
    except:
        return False
    else:
        outputs = handleDataFromPage(soup)
        return outputs