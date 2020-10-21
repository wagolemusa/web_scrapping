from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
import time
import urllib.request

class AmazonBot(object):

	def __init__(self, items):
		self.amazon_url = "https://www.amazon.ca/"
		self.items = items
		self.driver = webdriver.Chrome('/home/refuge/code/scraping/soup/chromedriver')
		self.driver.get(self.amazon_url)

	def search_items(self):
		urls = []
		prices = []
		names = []
		for item in self.items:
			# print("%s searching for %(item)") 
			self.driver.get(self.amazon_url)
			search_input = self.driver.find_element_by_id("twotabsearchtextbox")
			search_input.send_keys(item)
			time.sleep(2)

			search_button = self.driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]')
			search_button.click()
			time.sleep(2)

			# first_result = self.driver.find_element_by_class_name('sb_Azvq332I.sb_ji55L-0S.sb_1-64HM9_')
			# first_result = self.driver.find_element_by_id('data-click-index')
			# asin = first_result.get_attribute("data-click-asin")
			# asin = self.driver.find_element_by_link_text('data-click-asin')
			# print(asin)	
			asin= "B081P5NG1J"
			url = "https://www.amazon.ca/dp/" + asin
			# print(url)
			# url = find_element_by_xpath('//*[@id="38b37130-7a54-4ec8-b371-307a549ec80b"]')
			price = self.get_product_price(url)
			name = self.get_product_name(url)

			prices.append(price)
			urls.append(url)
			names.append(name)

			print(price)
			print(url)
			print(name)

			time.sleep(2)

		return prices, urls, names

	def get_product_price(self, url):
		self.driver.get(url)
		try:
			price = self.driver.find_element_by_id("priceblock_ourprice").text
		except:
			pass
		try:
			price = self.driver.find_element_by_id("priceblock_dealprice").text
		except:
			pass

		if price is None:
			price = "Not available"

		else:
			non_decimal = re.compile(r'[^\d.]+')
			price = non_decimal.sub('', price)
		return price

	def get_product_name(self, url):
		self.driver.get(url)
		try:
			product_name = self.driver.find_element_by_id("productTitle").text
		except:
			pass
		if product_name is None:
			product_name = "Not available"
		return product_name


# items = ["toothpaste"]
# amazon_bot = AmazonBot(items)
# amazon_bot.search_items()