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
iurl=''
vurl=''
ft = codecs.open("greece.txt","w",encoding="utf-8")
ss = api.user_timeline(id=twi_id,count=100)
for status in ss:
    #print status.author, status.user
    sid = status._json['id']
    stext = status.text.encode('utf-8')
    stext = stext.replace('\n',' ')
    #api.retweet(sid)
    #print status._json['media_url']
    #surl = status._json['entities']['media'][0]['media_url_https']
    #tweepy.Cursor(api.search, q="#hashtag", count=5, include_entities=True)
    if 'media' in status.entities:
        for image in  status.entities['media']:
            iurl = image['media_url_https']
    #if 'extended_entities' in status:
    
            #print iurl
    #print status._json
    line = line + twi_id+'||'+str(sid)+'||'+stext+'||'+iurl+'\n'
    #json.dump(status._json,ft)
#print line
#print surl
ft.write(line)
