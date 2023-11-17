import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd


# Create an URL object
url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

# Create object page
page = requests.get(url)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')

# Obtain information from tag <table>
table1 = soup.find('table', id='wikitable sortable jquery-tablesorter')
table1

# Obtain every title of columns with tag <th>
headers = []
for i in table1('th'):
    title = i.text
    headers.append(title)