import threading
import time
import json

def crawl(sub, reddit, sender, run_event):
    print(sub.name, "STARTED.")
    start_time = time.time()
    life_time = sub.life_time + start_time
    posts = []
    
    file = []
    if sub.store_on_notify:
        file = open("%s_notifications.txt"%sub.name[2:], 'w+')
    while run_event.is_set() and (sub.life_time == 0 or time.time() < life_time):
        new_posts = check_new(sub, reddit, posts)

        if sub.store_on_notify:
            for post in new_posts:
                file.write("{}\n".format(json.dumps(post)))

        posts = [p for p in posts if p[1]+sub.post_life_time > time.time()]

        if len(new_posts):
            notify_new(sub, new_posts, sender)
        last_notify = time.time()
        while run_event.is_set() and time.time() < life_time and time.time() < last_notify+sub.crawl_rate:
            time.sleep(1)

    new_posts = check_new(sub, reddit, posts)

    if sub.store_on_notify:
        for post in new_posts:
            file.write("{}\n".format(json.dumps(post)))

    if len(new_posts):
        notify_new(sub, new_posts, sender)

    notify_done(sub, sender)
    if sub.store_on_notify:
        file.close()
    print(sub.name, " FINISHED.")

def check_new(sub, reddit, posts):
    new_posts = []
    
    sub_posts = reddit.subreddit(sub.name[2:])
    sort_method = getattr(sub_posts, sub.sort_by.lower())
    found_ids = [p[0] for p in posts]
    for post in sort_method():
        if post.id in found_ids:
            posts = [(k, v) if (k!=post.id) else (post.id, time.time()) for (k,v) in posts]
        elif any(word in post.title or word in post.selftext for word in sub.key_words):
            posts.append((post.id, time.time()))
            new_posts.append({
                "title":post.title,
                "url":post.url,
                "time":post.created_utc
            })
    return new_posts

def notify_new(sub, posts, sender):
    for recipient in sub.recipients:
        sender.send_posts(recipient, sub, posts)

def notify_done(sub, sender):
    for recipient in sub.recipients:
        sender.send_msg(recipient, "%s has finished"%sub.name, "")

def start(subreddits, reddit, sender):
    threads = []
    run_event = threading.Event()
    run_event.set()
    for sub in subreddits:
        threads.append(threading.Thread(target=crawl, args=(sub, reddit, sender, run_event), name=sub.name))
    for thread in threads:
        thread.start()
    
    try:
        while len(threads) > 0:
            threads[0].join()
            threads = threads[1:]
    except KeyboardInterrupt:
        print("\nShutting down notify threads...")
        run_event.clear()
        for thread in threads:
            thread.join()
        print("DONE.")

        exit(0)



