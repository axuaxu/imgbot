#https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
import requests
import os
import tweepy
from time import sleep
from credentials import *
import sys
import codecs
import json

reload(sys)
sys.setdefaultencoding('utf-8')

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#4502
twi_id = "Amazing_Greece"
line = "" 
ft = codecs.open("greece.txt","w",encoding="utf-8")
ss = api.user_timeline(id=twi_id,count=100)
for status in ss:
    #print status.author, status.user
    sid = status._json['id']
    stext = status.text.encode('utf-8')
    #api.retweet(sid)
    #print status._json['media_url']
    surl = status._json['entities']['media'][0]['media_url_https']
     
    #print status._json
    line = line + twi_id+','+sid+','+stext+','+surl+',\n'
    #json.dump(status._json,ft)
