import requests
from bs4 import BeautifulSoup

sauce = requests.get('https://pythonprogramming.net/parsememcparseface/')

soup = BeautifulSoup(sauce.content, 'xml')

for  url in soup.find_all('loc'):
	print(url.text)
