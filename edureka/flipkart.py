from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.chrome("/usr/lib/chromium-browser/chromedriver")

products = []
prices = []
ratings = []
driver.get("https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop|Laptops&requestId=c398ac17-09c7-471d-8923-e0e4a08606ed&as-backfill=on")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':'_31qSDS'}):
	name = a.find('div', attrs={'class':'_3wU53n'})
	price = a.find('div', attrs={'class':'_1UoZlX_6BWGkk_2rQ-NK'})
	rating = a.find('div', attrs={'class':'hGSR34'})
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)

	df=pd.DataFlame({'Product Name' : products, 'Price':prices, 'Rating':ratings})
	df.to_csv('products.csv', index=False, encoding='utf-8')