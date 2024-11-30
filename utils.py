import re

def format_text(text):
    return text.replace(" ", "+")

def get_price(text):
    price = re.search(r"\d+\.?\d*", text).group()
    return price