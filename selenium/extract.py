from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class CraiglistScraper(object):
	def __init__(self, location, postal, max_price, radius):
		self.location = location
		self.postal = postal
		self.max_price = max_price
		self.radius = radius
		self.driver = webdriver.Chrome('/home/refuge/code/scraping/soup/chromedriver')
		self.delay = 3
		self.url = "https://%s.craigslist.org/search/sss?search_distance=%s&postal=%s&max_price=%s" %(location,postal,radius,max_price)
	
	def load_craigslist(self):
		self.driver.get(self.url)
		try:
			wait = WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_located((By.ID, "searchform")))
			print("pag is ready")
		except TimeoutException:
			print("Location took too much time")

	def extract_post_infomation(self):
		all_posts = self.driver.find_elements_by_class_name("result-row")

		dates = []
		titles = []
		prices = []

		for post in all_posts:
			title = post.text.split("$")
			# print(title)
			if title[0] == '':
				title = title[1]
			else:
				title = title[0]
			title = title.split("\n")
			price = title[0]
			title = title[-1]

			title = title.split(" ")
			month = title[0]
			day = title[1]
			title = ' '.join(title[2:])
			date = month + " " + day

			# print("PRICE: " + price)
			# print("TITLE: " + title)
			# print("DATE: " + date)

			# storing them in alist
			titles.append(title)
			prices.append(price)
			dates.append(date)
		return titles, prices, dates
	

	def extract_post_urls(self):
		url_list = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, "lxml")
		# get the url plus the class 
		for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
			# only grabing the href
			print(link["href"])
			url_list.append(link["href"])
		return url_list

	def quit(self):
		self.driver.close()

location = "sfbay"
postal = "94201"
max_price = "500"
radius = "5"
scraper = CraiglistScraper(location, postal, max_price, radius)
scraper.load_craigslist()
titles, prices, dates, = scraper.extract_post_infomation()
print(dates)
# scraper.extract_post_urls()
# scraper.quit()