#https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
import requests
import os
import tweepy
from time import sleep
import sys
import codecs
import json
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

# Access and authorize our Twitter credentials from credentials.py


#4502

ft = codecs.open("greece.txt","r",encoding="utf-8")
for line in ft:
       # print line.encode('utf-8')
    t = line.split('||')
    url = t[3]
    #print t[3],t[4]
    if '.jpg' in t[3]:
    	narr = t[3].split('/')
    	img = narr[-1]
    	iname = '.\\travelpic\\greece\\'+img
    	print iname
    	urllib.urlretrieve(t[3],iname)
    if '.mp4' in t[4]:
    	varr = t[4].split('/')
    	video = varr[-1].replace('\n','')
        vname =  '.\\travelvideo\\greece\\'+video
        urllib.urlretrieve(t[4],vname)
        print vname