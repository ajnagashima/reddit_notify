import threading
import time

def crawl(sub, reddit, run_event):
    print(sub.name, "STARTED.")
    start_time = time.time()
    life_time = sub.life_time*60 + start_time
    posts = []
    
    with open("%s_notifications.txt"%sub.name[2:], 'w+') as file:
        while run_event.is_set() and (sub.life_time == 0 or time.time() < life_time):
            check_new(sub, reddit, posts)
            last_notify = time.time()
            while run_event.is_set() and time.time() < life_time and time.time() < last_notify+sub.crawl_rate:
                time.sleep(1)
        check_new(sub, reddit, posts)
    notify_done()
    print(sub.name, " FINISHED.")

# TODO
def check_new(sub, reddit, posts):
    print("check_new called")

# TODO
def notify_done():
    print("notify_done called")

def start(subreddits, reddit):
    threads = []
    run_event = threading.Event()
    run_event.set()
    for sub in subreddits:
        threads.append(threading.Thread(target=crawl, args=(sub, reddit, run_event), name=sub.name))
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



