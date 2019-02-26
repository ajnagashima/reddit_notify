class Subreddit:
    def extract_features(self,
            crawl_rate=60, 
            sort_by='NEW', 
            recipient='', 
            store_on_notify=False, 
            key_words='', 
            delay=0):
        self.crawl_rate = crawl_rate
        self.sort_by = sort_by
        self.recipient = recipient
        self.store_on_notify = store_on_notify
        self.key_words =  key_words
        self.delay =  delay

    def __str__(self):
        return (str(self.name) + ":\n\t" +
            str(self.crawl_rate)+ ",\n\t" +
            str(self.sort_by) + ",\n\t" +
            str(self.recipient) + ",\n\t" +
            str(self.store_on_notify) + ",\n\t" +
            str(self.key_words) + ",\n\t" +
            str(self.delay))

    def __init__(self, data):
        self.name = data[0]
        if self.name[0:2] != "r/" or "/" in self.name[2:]:
            print("ERROR: bad subreddit name\nEXPECTED: 'r/...'\nRECEIVED: ",self.name)
            exit()
        self.extract_features(**data[1])
        print(self)

