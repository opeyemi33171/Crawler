import praw
import requests
import os
import ctypes


counter = 0

r = praw.Reddit(user_agent='windows:Crawler:1.0 (by /u/opeyemi94)')

post = r.get_subreddit('earthporn').get_top(limit=10)
for url in post:
    global counter
    if str(url.url).endswith('.jpg') or str(url.url).endswith('.png'):
        image = requests.get(url.url)
        image_file = open('image{}.jpg'.format(counter), 'wb')
        for chunk in image.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        counter += 1


ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("image0.jpg"), 1 | 2)