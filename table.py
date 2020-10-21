import requests
from bs4 import BeautifulSoup

sauce = requests.get('https://pythonprogramming.net/parsememcparseface/')

soup = BeautifulSoup(sauce.content, 'html.parser')

table = soup.table
# print(table.text)

table_rows = table.find_all('tr')
for tr in table_rows:
	td = tr.find_all('td')
	row = [i.text for i in td]
	print(row)