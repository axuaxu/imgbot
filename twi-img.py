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

def tweet_image(url, message):
    #api = twitter_api()
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

url = "http://media02.hongkiat.com/raspberry-pi-projects/1-lappi-netbook.jpg"
fn = ".\img\paul-cezanne\pierrot-and-harlequin-mardi-gras-1888.jpg"
message = "landscape"
#tweet_image(url,message)

api.update_with_media(fn, status=message)
#photo = open('/path/to/file/image.jpg', 'rb')
#photo = open('cagnes-landscape-1910-1.jpg', 'rb')
#response = Twitter.upload_media(media=photo)
#Twitter.update_status(status='Checkout this cool image!', media_ids=[response['media_id']])

#img = "http://animalia-life.com/data_images/bird/bird1.jpg"
#api.status(status="%s Nice one" % img)