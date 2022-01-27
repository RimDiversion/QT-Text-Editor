"""
This allows you to send a copy of the file you are working with to your email.
You need to set up a .env file with attributes 'ADDRESS=<your_email_address>' and
'PASSWORD=<your_password>'. Note that you may need to turn off some security settings
from your email provider so make sure you understand those implications before using.
"""

import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, content):
    """sends the content to pre-determined email address"""
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

    mail.close()
