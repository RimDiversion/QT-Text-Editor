import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

def send_email(recipient, subject, content):
    username = os.environ.get('ADDRESS')
    password = os.environ.get('PASSWORD')
    sender = os.environ.get('ADDRESS')
    header = 'To:' + recipient + '\n' + 'From: ' + sender + '\n' + 'Subject: ' + subject + '\n'

    message = header + content

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(username, password)

    mail.sendmail(sender, recipient, message)
    print('message sent')

    mail.close

if __name__ == '__main__':
    recipient = 'machine.rim@gmail.com'
    subject = 'test'
    content = "Hello world"
    send_email(recipient, subject, content)
