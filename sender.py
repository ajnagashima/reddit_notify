import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

class Sender:
    def send_posts(self, toaddr, subreddit, posts):
        msg = MIMEMultipart()
        msg['From'] = self.email_addr
        msg['To'] = toaddr
        msg['Subject'] = "New posts from %s"%subreddit.name
        msg['Date'] = formatdate(localtime=True)

        body = ""
        for post in posts:
            body = (body + "Posted at " + 
                str(formatdate(post['time'], localtime=True)) +":\n"+ 
                str(post['title']) + "\n" + 
                str(post['url']) + "\n\n")

        msg.attach(MIMEText(body, 'plain'))
        server = []
        try:
            server = smtplib.SMTP(self.mail_server, 25)
        except:
            print("FATAL: no mail serveri conf")
            exit(1)
        server.starttls()
        text = msg.as_string()
        server.sendmail(self.email_addr, toaddr, text)
        server.quit()


    def send_msg(self, toaddr, subject, body):
        print("send message called")

    def __init__(self, data):
        try:
            self.email_addr = data['email_addr']
        except:
            print("WARN: no email address in conf")
        try: 
            self.mail_server = data['mail_server']
        except:
            print("WARN: no mail server in conf")
