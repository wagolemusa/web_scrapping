import requests
from bs4 import BeautifulSoup

sauce = requests.get('https://pythonprogramming.net/parsememcparseface/')

soup = BeautifulSoup(sauce.content, 'html.parser')

nav = soup.nav
# for url in nav.find_all('a'):
# 	print(url.get('href'))

# body = soup.body
# for paragraphy in body.find_all('p'):
# 	print(paragraphy.text)


# for h in body.find_all('li'):
# 	print(h.text)

# for  div in soup.find_all('div'):
# 	print(div.text)

for div in soup.find_all('div', class_='body'):
	print(div.text)