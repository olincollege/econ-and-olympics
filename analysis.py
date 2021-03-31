import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table")
soup = BeautifulSoup(page.content, 'html.parser')
target_data = soup.find(id="mw-content-text")
tables = target_data.find_all(class_ = "wikitable sortable")
print(tables)

get_medals()