#https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
import requests
import os
import tweepy
from time import sleep
from creaxu import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

 

ss = api.user_timeline(id='lisaeme75659217',count=1)
for status in ss:
    #print status.author, status.user
    sid = status._json['id']
    api.retweet(sid)
    #print status._json['id']
    #print status._json