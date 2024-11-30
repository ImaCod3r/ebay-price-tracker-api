from bs4 import BeautifulSoup
import requests

url = "https://www.ebay.com/sch/"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" }
params = { "_nkw": "Macbook+pro" }

response = requests.get(url, headers=headers, params=params)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

titles = soup.select(".s-item__wrapper .s-item__title")
prices = soup.select(".s-item__wrapper .s-item__price")
links = soup.find_all(class_="s-item__link")

for title, price, link in zip(titles, prices, links):
    print("-" * 120)
    print(title.text)
    print(price.text)
    print(link.get('href'))