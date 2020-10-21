from amazon_bot import AmazonBot
# from email_alert import EmailAlert 
from send_email import send_email

import gspread
# import cryptography.exceptions
from oauth2client.service_account import ServiceAccountCredentials

class PriceUpdater(object):
	def __init__(self, spreadsheet_name):

		self.item_col = 1
		self.price_col = 2
		self.frequency_col = 3
		self.url_col = 4
		self.product_name_col = 3

		scope = ['https://spreadsheets.google.com/feeds',
							'https://www.googleapis.com/auth/drive']

		creds = ServiceAccountCredentials.from_json_keyfile_name('clientgoogle.json', scope)
		client = gspread.authorize(creds)

		self.sheet = client.open('ProductPrice').sheet1

	def process_item_list(self):
		items = self.sheet.col_values(self.item_col)[1:]
		amazon_box = AmazonBot(items)
		prices, urls, names = amazon_box.search_items()

		print("Updating spreedsheet.")
		for i in range(len(prices)):
			self.sheet.update_cell(i+2, self.price_col, prices[i])
			self.sheet.update_cell(i+2, self.url_col, urls[i])
			self.sheet.update_cell(i+2, self.product_name_col, names[i])


price_updater = PriceUpdater("ProductPrice")
price_updater.process_item_list()


subject = "Google Sheets Updated"
msg =  "This is a message to let you know that the spreedsheet has been updated"
send_email(subject, msg)

# stuff = sheet.get_all_records()
# print(stuff)
