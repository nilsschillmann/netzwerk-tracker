#%%
import requests
import time
import random
from multiprocessing import Pool
import platform
import os




# %%
url_list = ["http://www.google.com",
            "https://stackoverflow.com",
            "https://twitter.com",
            "http://amazon.de",
            "http://postbank.de",
            "http://wikipedia.org",
            "http://ebay.de",
            "http://instagram.com",
            "http://bild.de",
            "http://t-online.de",
            "http://web.de",
            "http://gmx.net",
            "http://spiegel.de",
            "http://wetter.com",
            "http://focus.de",
            "http://paypal.com",
            "http://dhl.de",
            "http://samsung.com",
            "http://otto.de",
            "http://welt.de",
            "http://idealo.de",
            "http://reddit.com",
            "http://chip.de",
            "http://tagesschau.de",
            ]
url_size = 4
timeout = 5
sleeptime = 10
file_path = os.path.expanduser(".")
filename = "/".join([file_path, "track.txt"])
#%%

def check_connection(url):
    try:
        requests.get(url, timeout=timeout)
        return True
    except:
        return False
#%%
def main():
    was_connected = None
    last_connection_text = ""
    while True:
        now = time.time()
        urls = random.sample(url_list, url_size)
        
        with Pool() as p:
            connected = any(p.map(check_connection, urls))
        
        connection_text = f"{now}; {connected}; {urls}\n"
        if was_connected != connected:
            print(last_connection_text, end="")
            print(connection_text, end="")
            with open(filename, "a") as file:
                file.write(last_connection_text)
                file.write(connection_text)
                
        last_connection_text = connection_text
        was_connected = connected
        
        time_to_sleep = sleeptime - (time.time() - now)
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)
        
    
if __name__ == '__main__':
    main()
# %%