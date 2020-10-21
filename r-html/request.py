from requests_html import HTMLSession

session = HTMLSession

start = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'

r = session.get(start)
print(r) 