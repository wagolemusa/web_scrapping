import gspread
# import cryptography.exceptions
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
					'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('clientgoogle.json', scope)
client = gspread.authorize(creds)

sheet = client.open('ProductPrice').sheet1
stuff = sheet.get_all_records()
print(stuff)
