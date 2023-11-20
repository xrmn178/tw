import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, "lxml")

a = soup.findAll({'th' : True, 'a' :True})
print(a)







