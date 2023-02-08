import requests
from bs4 import BeautifulSoup as BS
import re

link = input("enter a link:")
r = requests.get(link)
html = BS(r.content, 'html.parser')

a = html.select_one('.desc-price-value').text
m = re.findall('от (.* )₸', a)
price = re.sub(r"\s+", "", m[0])
print("price:", int(price))

