import sys

class Subreddit:
    def extract_features(self,
            crawl_rate=60, 
            sort_by='NEW', 
            recipient='', 
            store_on_notify=False, 
            key_words='', 
            delay=0,
            life_time=0, 
            post_life_time=24):
        try:
            if int(crawl_rate) < 0:
                print("ERROR: crawl_rate cannot be negative")
                return 1
        except:
            print("ERROR: crawl_rate is NaN")
            return 1

        if str(sort_by).lower() not in ["new", "hot", "top"]:
            print("ERROR: sort_by must be 'NEW', 'HOT' or 'TOP'")
            return 1

        if not isinstance(store_on_notify, bool):
            print("ERROR: store_on_notify is not type bool")
            return 1

        try:
            if int(delay) < 0:
                print("ERROR: delay cannot be negative")
                return 1
        except:
            print("ERROR: delay is NaN")
            return 1

        try:
            if int(life_time < 0):
                print("ERROR: life_time cannot be negative")
                return 1
        except:
            print("ERROR: life_time is NaN")
            return 1

        try:
            if int(post_life_time < 0):
                print("ERROR: life_time cannot be negative")
                return 1
        except:
            print("ERROR: post_life_time is NaN")
        
        self.crawl_rate = int(crawl_rate)
        self.sort_by = sort_by
        self.recipient = recipient.split(",")
        self.store_on_notify = bool(store_on_notify)
        self.key_words = key_words.split(",")
        self.delay = int(delay)
        self.life_time = int(life_time)
        self.post_life_time = int(post_life_time)

        return 0

    def __str__(self):
        return (str(self.name) + ":\n\t" +
            str(self.crawl_rate)+ ",\n\t" +
            str(self.sort_by) + ",\n\t" +
            str(self.recipient) + ",\n\t" +
            str(self.store_on_notify) + ",\n\t" +
            str(self.key_words) + ",\n\t" +
            str(self.delay) + ",\n\t" +
            str(self.life_time) + ",\n\t" +
            str(self.post_life_time))

    def __init__(self, data):
        self.name = data[0]
        if self.name[0:2] != "r/" or "/" in self.name[2:]:
            print("ERROR: bad subreddit name\nEXPECTED: 'r/...'\nRECEIVED: ",self.name)
            sys.exit(1)

        if self.extract_features(**data[1]) == 1:
            sys.exit(1)

#       print(self)

