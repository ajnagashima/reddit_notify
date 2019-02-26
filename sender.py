class Sender:
    # TODO
    def send(self, toaddr, subreddit, posts):
        print("send hit")

    def __init__(self, data):
        try:
            self.email_addr = data[1]['email_addr']
        except:
            print("WARN: no email address in conf")
        try:
            self.sms_number = data[1]['sms_number']
        except:
            print("WARN: no sms number in conf")

