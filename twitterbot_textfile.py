# Import our Twitter credentials from credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file verne.txt (or your chosen file) for reading
my_file = open('verne.txt', 'r')
#ttps://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library
# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Create a for loop to iterate over file_lines
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(900)
             else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(32)

tweet()