# package praw
import praw
# package pyyaml
import yaml
# import subreddit
from subreddit import Subreddit

def main():
    config = importConfig()
    creds = []
    sub_data = []
    print("Extracting credentials...", end = "")
    try:
        creds = config["credentials"]
    except:
        error("credentials not found, use keyword 'credentials' in config.yaml")
    print("DONE.")

    print("Extracting subreddits...", end = "")
    try:
        sub_data = config["subreddits"]
    except:
        error("subreddits not found, use keyword 'subreddits' in config.yaml")
    print("DONE.")

    subreddits = []
    for sub in sub_data.items():
        subreddits.append(Subreddit(sub))



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
        error(exc)


def error(msg):
    print("\nERROR: ", msg)
    exit()

if __name__ == "__main__":
    main()
