import praw
import requests
import os
import ctypes


counter = 0

r = praw.Reddit(user_agent='windows:Crawler:1.0 (by /u/opeyemi94)')
r.login('opeyemi94', 'bankole1994')

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

''' this bit doesn't work
image_path = 'C:/Users/opeyemi/Desktop/Crawler/images/image0.jpg'
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
'''