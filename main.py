#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
tweetsFile = str(sys.argv[1])
minutes = str(sys.argv[2])
 
#Connect with Twitter API:
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(tweetsFile,'r')
f=filename.readlines()
filename.close()
 
#Tweets every (user inputted) minutes
for line in f:
    api.update_status(status=line)
    time.sleep(minutes / 60)
