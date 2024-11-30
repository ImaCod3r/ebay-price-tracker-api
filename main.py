from bs4 import BeautifulSoup
import utils
import requests

configs = {
    "url": "https://www.ebay.com/sch/",
    "headers": { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" }
}

def make_request(configs, query):
    query = utils.format_text(query)
    url = configs["url"] + query
    headers = configs["headers"]
    
    response = requests.get(url, headers=headers)
    html = response.content
    
    return html

def scrap_page(html):
    soup = BeautifulSoup(html, "html.parser")
    
    titles = soup.select(".s-item__wrapper .s-item__title")
    prices = soup.select(".s-item__wrapper .s-item__price")
    links = soup.select(".s-item__wrapper .s-item__link")
    
    return zip(titles, prices, links)

def display_items(items):
    for title, price, link in items:
        print("-" * 120)
        print(title.text)
        print(utils.get_price(price.text))
        print(link.get('href'))
        
def main():
    query = input("Product name:")
    
    html = make_request(configs, query)
    items = scrap_page(html)
    
    display_items(items)

if __name__ == "__main__":
    main()