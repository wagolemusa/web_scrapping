import requests
from bs4 import BeautifulSoup
import pandas as pd

strat_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'
download_html = requests.get(start_url)
soup = BeautifulSoup(download_html.text)

with open('download_html', 'w') as file:
    file.write(soup.prettiy())