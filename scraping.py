import requests
from bs4 import BeautifulSoup

sauce = requests.get('https://pythonprogramming.net/parsememcparseface/')

soup = BeautifulSoup(sauce.content, 'html.parser')

# print(soup)
# print(soup.title.string)
# print(soup.find_all('p'))

# for pragraph in soup.find_all('p'):
# 	# print(pragraph.string)
# 	print(pragraph.text)

# print(soup.get_text())

for url in soup.find_all('a'):
	print(url.get('href'))