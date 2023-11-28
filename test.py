import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

# Найдем таблицу с данными
table = soup.find('table', {'class': 'wikitable'})

# Итерируемся по строкам таблицы
for row in table.find_all('tr')[1:]:  # Пропускаем заголовок
    columns = row.find_all('td')
    if len(columns) == 0:
        continue  # Пропустим строки заголовка и другие пустые строки

#website =
#popularity =
#frontend =
#backend =
#database =
#notes =
52





