import re

def getNumericPrice(text):
    price = float(re.search(r"\d+\.?\d*", text).group())
    return price

def getAveragePrice(prices):
    return sum(map(float, prices)) / len(prices)