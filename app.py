from smtplib import SMTP
from getpass import getpass


sender = "_______@gmail.com"
receivers = ['_____@gmail.com', '________@gmail.com']

message = """
Test email
Ignore it
"""
username = sender
password = getpass()

try:
    SMTPobj = SMTP('smtp.gmail.com:587')
    SMTPobj.starttls()
    SMTPobj.login(username, password)
    SMTPobj.sendmail(sender, receivers, message)
    SMTPobj.quit()
    print("Email sent.")
except Exception as e:
    print("Email sending failed due to: ", e)
