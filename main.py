#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
#Connect with Twitter API:
CONSUMER_KEY = 'XfZ6EPKOrECwzlSe0Suyupmje'
CONSUMER_SECRET = 'R0fQRA6MA4XFe2iC0hrDZhBWYHZvvv1UXHdxITWBDbxaVdAYnG'
ACCESS_KEY = '2161610844-s104cLX1nOlpwoTJnMhPAfKssRJ7inBQtEN36hb'
ACCESS_SECRET = 'dG12nw71s8enHe8IBRODet7smM51sgdP570B3UjyQuGUD'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
#Tweet every 15 minutes
for line in f:
    api.update_status(status=line)
    time.sleep(900)