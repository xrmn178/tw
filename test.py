import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd


# Create an URL object
url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

# Create object page
page = requests.get(url)
print(page)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')


#a = soup.find('div', class_='wm_parser_output').find_all('tr')
#result = {}

print(a)

