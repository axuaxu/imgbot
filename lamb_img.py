#https://medium.com/the-python-backend/hassle-free-python-lambda-deployment-tutorial-script-9c65bcf47e26
import boto3
from boto3.dynamodb.conditions import Key, Attr
from random import randint

import os
import tweepy
from credentials import *
import sys

def lamb_img(event, context):

 reload(sys)
 sys.setdefaultencoding('utf-8')

 consumer_key='rD7LSDlI4TF3Iw1p9Q9xQ3lCh'
 consumer_secret ='pMvAJIUAxMzDyZjKEqHSo1k7qEHyo4sHmYTdEmAWTDplq4Zkfu'
 access_token= '899308310461075457-LxqERAtAfzgWbXHjT1k65MDsntNgxqz'
 access_token_secret= 'IMz3fbb0eop316Wid7JaHvLSfNnzcqRiv4Et9qlv5F56M'
 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)
 api = tweepy.API(auth)

 s3 = boto3.resource('s3')

# Get the service resource.
 dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
 table = dynamodb.Table('imglist')
 response = table.scan(
    FilterExpression=Attr('name').begins_with('images')
 )
 count = len(response['Items'])
 i = randint(0,count)
#print i
 item  =  response['Items'][i]
#print(item['name'])
 nstr =  item['name'].encode('utf-8').replace('\n','')
 narr = nstr.split('/')
#print(len(narr))
 if  len(narr)==3:
    painter = narr[1]
    name = painter.split('-')
    lastname = name[-1]
    fullname = painter.replace('-','')
    pic = narr[2]
    pic=  pic.split('.')[0]
    painter = painter.replace('-',' ')
    pic = pic.replace('-',' ')
    print (painter)
    print (pic)
    status =  painter+'\n'+pic
    status = status.title()
    hashstr = '\n#art '+'#painting '+'#'+fullname+' '+'#'+lastname
    status = status + hashstr
    myb = "axufile"
    tmpf = '/tmp/'+narr[2]
#     print(myb,nstr,tmpf)
    boto3.client('s3').download_file(myb,nstr,tmpf)
    file = open(tmpf,'rb')
    api.update_with_media(tmpf, status=status)
    table.delete_item(
         Key={
           'name': item['name'],
       })
