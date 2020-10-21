from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as BC
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

# driver = webdriver.Firefox('/home/refuge/code/scraping/selenium/geckodriver')
driver = webdriver.Chrome('/home/refuge/code/scraping/soup/chromedriver')

driver.get("http://econpy.pythonanywhere.com/ex/001.html")

buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')

prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# print out all the buyers and prices on the current pages

num_page_items = len(buyers)
for i in range(num_page_items):
	print(buyers[i].text + " : "+ prices[i].text)

# print(result)
driver.close()