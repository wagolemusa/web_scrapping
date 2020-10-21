from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as BC
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time
import csv
MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")


with open('result.csv', 'w') as f:
	f.write("Buyers, Price \n")

for i in range(1, MAX_PAGE_NUM +	 1):
	page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
	driver = webdriver.Chrome('/home/refuge/code/scraping/soup/chromedriver')
	url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"
	driver.get(url)

	buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
	prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

	num_page_items = len(buyers)
	with open('results.csv', 'a') as f:
		for i in range(num_page_items):
			f.write(buyers[i].text + "," + prices[i].text + "\n")

driver.close()