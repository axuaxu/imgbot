#https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
import requests
import os
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

 

stuff = api.user_timeline(screen_name = 'lisaeme75659217', count = 1, include_rts = True)
for status in stuff:
    #print status.author, status.user
    print status._json
#photo = open('/path/to/file/image.jpg', 'rb')
#photo = open('cagnes-landscape-1910-1.jpg', 'rb')
#response = Twitter.upload_media(media=photo)
#Twitter.update_status(status='Checkout this cool image!', media_ids=[response['media_id']])

#img = "http://animalia-life.com/data_images/bird/bird1.jpg"
#api.status(status="%s Nice one" % img)