class Sender:
    # TODO
    def send_posts(self, toaddr, subreddit, posts):
        print("send posts called")

    def send_msg(self, toaddr, subject, body):
        print("send message called")

    def __init__(self, data):
        try:
            self.email_addr = data['email_addr']
        except:
            print("WARN: no email address in conf")
        try:
            self.sms_number = data['sms_number']
        except:
            print("WARN: no sms number in conf")

