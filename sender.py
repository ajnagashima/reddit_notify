class Sender:
    # TODO
    def send(self, toaddr, subreddit, posts):
        print("send hit")

    def __init__(self, data):
        try:
            self.email_addr = data.email_addr
        except:
            print("WARN: no email address in conf")
        try:
            self.sms_number = data.sms_number
        except:
            print("WARN: no email address in conf")

