# reddit_notify
A bot the notifies a user through text or email when certain keywords are found on a subreddit

## Setup

### Python Dependencies

Using virtualenv is recommended when installing packages for python.
* `praw`
* `smtplib`
* `email`
* `threading`
* `json`

### Setting up PRAW

Create a bot through reddit to get a client id and secret for use with this app.

### conf.yaml
Conf.yaml allows users to configure the reddit_notify bot through the following parameters:

`credentials`
* `client_id` - The client for the reddit bot
* `client_secret` - The client secret assigned by reddit for this bot
* `user_agent` - The name given to reddit for bot

`subreddits`
For each subreddit, a new nested field should be added the follows the format `r/<subreddit>`, the props for each subreddit include: 
* `crawl_rate` - Used to set the number of seconds between each crawl, `crawl_rate` >= 0
* `sort_by` - The sort used for PRAW to retrieve posts, only `NEW`, `HOT`, and `TOP` are accepted
* `recipient` - The email to receive notifications for this subreddit, comma separated for multiple recipients
* `store_on_notify` - A boolean used to determine if post information should be saved to a txt file on retrieval, a true or false value
* `key_words` - The keywords that PRAW uses to find posts, comma separated for multiple keywords
* `delay` - The delay used to accumulate posts before sending in seconds, `delay` >= 0
* `life_time` - Number of days for the bot to operate, `life_time` >= 0
* `post_life_time` - Number of hours the post is stored internally to prevent duplicate sending, `post_life_time` >= 0

`mail`
* `email_addr` - The email that the mail comes from
* `mail_server` - The mail server used to send this email
* `mail_server_port` - The port used to connect to the mail server (usually 25)
