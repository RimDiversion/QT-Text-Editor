import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, content):
    """sends the content to email set up in en .env with adress and password"""
    username = os.environ.get('ADDRESS')
    password = os.environ.get('PASSWORD')
    header = 'To:' + username + '\n' + 'From: ' + username + '\n' + 'Subject: ' + subject + '\n'

    message = header + content

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(username, password)

    mail.sendmail(username, username, message)
    print('message sent')

    mail.close
