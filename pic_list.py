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
maxid = '867345600366424067'
fout = codecs.open("pic_url.txt","w",encoding="utf-8")
ftwi = open('pictwi_list.txt','r')
line = ""
for twi_id in ftwi:
         twi_id = twi_id.replace('\n','')
         ss = api.user_timeline(id=twi_id, max_id = maxid, count=20)
         for status in ss:
             iurl = ''
             vurl = ''
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
                   if 'video' in iurl:
                       if 'media' in status.extended_entities:
                            for video in status.extended_entities['media']:
                                if 'video_info' in video:
                                   vurl = video['video_info']['variants'][1]['url']
                                   print vurl
    
                                  #print iurl
                                  #print status._json
             line = line + twi_id+'||'+str(sid)+'||'+stext+'||'+iurl+'||'+vurl+'\n'
    #json.dump(status._json,ft)
#print line
#print surl
fout.write(line)
