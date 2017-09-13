#https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
import requests
import os
import tweepy
from time import sleep
import sys
import codecs
import json
from pymongo import MongoClient
 


reload(sys)
sys.setdefaultencoding('utf-8')

# Access and authorize our Twitter credentials from credentials.py


#4502
client = MongoClient()
db = client['travel_greece']
coll = db['heartouchingpic']

ft = codecs.open("heartouchingpic.txt","r",encoding="utf-8")
for line in ft:
       # print line.encode('utf-8')
    t = line.split('||')
    url = t[3]
    print t[3],t[4]
   
    doc = {
    "name": t[0],
    "tid": t[1],
    "desc": t[2],
    "imgurl": t[3],
    "videourl": t[4]
    }
 
    doc_id = coll.insert_one(doc).inserted_id

