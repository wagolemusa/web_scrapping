import smtplib
# import configemail
import config

class EmailAlert(object):
	""" Class sending notifications"""
	def __init__(self, subject, msg):
		self.subject = subject
		self.msg = msg

	def send_email(self):
		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(config.EMAIL_ADDRESS, config.PASSWORD)
			message = 'Subject: {} \n \n {}'.format(subject, msg)
			server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
			server.quit()
			print("Success: Email sent")
		except:
			print("Email failed to send")

email = EmailAlert("Google Sheets Updated", "This is a message to let you know that the spreedsheet has been updated")
email.send_email()