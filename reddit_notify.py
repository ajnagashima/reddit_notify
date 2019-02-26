import sys
# package praw
import praw
# package pyyaml
import yaml
# import subreddit
from subreddit import Subreddit
# import notify
import notify

from mail import Mail

def main():
    config = importConfig()
    creds = []
    sub_data = []

    print("Extracting credentials...", end = "")
    try:
        creds = config["credentials"]
    except:
        error("\ncredentials not found, use keyword 'credentials' in config.yaml")
    print("DONE.")

    print("Extracting subreddits...", end = "")
    try:
        sub_data = config["subreddits"]
    except:
        error("\nsubreddits not found, use keyword 'subreddits' in config.yaml")
    print("DONE.")

    print("Validating Subreddits...", end="")
    subreddits = []
    for sub in sub_data.items():
        subreddits.append(Subreddit(sub))
    print("DONE.")

    reddit = []
    try:
        reddit = praw.Reddit(
            client_id=creds['client_id'], 
            client_secret=creds['client_secret'],
            user_agent=creds['user_agent'])
    except:
        error("Bad Credentials")

    mail = []
    try:
        mail = Mail(config['mail'])
    except:
        print("WARN: no mail found in conf.yaml")

    notify.start(subreddits, reddit, mail)

def importConfig():
    print("Importing config.yaml...", end = "")
    try:
        with open("conf.yaml", 'r') as conf:
            try:
                config = yaml.load(conf)
                print("DONE.")
                return config
            except yaml.YAMLError as exc:
                error(exc)
    except Exception as exc:
        error("n"+str(exc))


def error(msg):
    print("ERROR: ", msg)
    sys.exit(1)

if __name__ == "__main__":
    main()
