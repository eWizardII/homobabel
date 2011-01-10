#!/usr/bin/env python

import tweepy

CONSUMER_KEY = 'FrF0MkzWEFgWvjFJQeFURg'
CONSUMER_SECRET = 'JORCs8eq3130QpMw8ogZB9WqHjwSWDBjPjQAEABVoQ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret
