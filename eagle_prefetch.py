#!/usr/bin/env python
"""
eagle_prefetch.py
Designed to scan Twitter for viable accounts, for established parameters
Selects the userd_ids of the top 100 followed and follower accounts

Solomon Abiola
http://www.ewizardii.com
"""

## Import Modules
import time
import json
import tweepy
from threading import Thread
from tweepy.cursor import Cursor



#Run main program
#Creates a thread of network calls to Twitter passes through VPN and Proxy


def lvl1():

    ## Thread loop - birdofprey

    class birdofprey(Thread):
        def __init__ (self,ip,api_name,oauth_token,oauth_token_secret):
            Thread.__init__(self)
            self.ip                 = ip
            self.api_name           = api_name
            self.oauth_token        = oauth_token
            self.oauth_token_secret = oauth_token_secret

        def run(self):
            ## OAuth Dance!

            CONSUMER_KEY    = '3y1428CJNYI3uqgW8oFcEA'
            CONSUMER_SECRET = 'GPpj8e6jOVkecaxfb5GmgIvI8ObnqYzo80oXt8v3c'

            auth            = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(self.oauth_token, self.oauth_token_secret)
            api             = tweepy.API(auth)

            api.proxy_host  = 'twitter' + str(self.api_name) + '-ewizardii.apigee.com'
            api.retry_count = 3
            api.retry_delay = 1
            

            ## Grab the seeds (i.e. the top 100 Twitter users ranging from @ladygaga - @womensweardaily

            i               = 0
            for null in range(0,1):
                while True:
                    try:
                        for friends in Cursor(api.followers_ids,screen_name=self.ip).items():
                            i = i + 1
                            with open('B:/Twitter/topusers.csv', mode='a') as a_file:
                                new_i  = ',' + str(friends)
                                a_file.write(new_i)
                    except tweepy.TweepError, e:
                        print "ERROR on " + str(self.ip) + " Reason: ", e
                        with open('B:/Twitter/errors.txt', mode='a') as a_file:
                            new_ii = "ERROR on " + str(self.ip) + " Reason: " + str(e) + "\n"
                            a_file.write(new_ii)
                    break

            print str(i) + " users found for " + str(self.ip) + " \n"
            print "Completed"

        def join(self,timeout=None):
            Thread.join(self, timeout)

    ## Necessary Variables

    source      = []
    delta       = 0
    api_name    = 1
    json_data2  = open("B:/Twitter/commodore.json")
    data2       = json.load(json_data2)

    json_data3  = open("B:/Twitter/top100.json")
    data3       = json.load(json_data3)

    ## Massive For-loop used to call the correct APIs and Twitter Users

    for host in range(0,67):
        ## User 1 in API
        ip                  = data3[host]['screen_name']
        oauth_token         = data2[0][str(delta)]['oauth_token']
        oauth_token_secret  = data2[0][str(delta)]['oauth_token_secret']
        urlv                = birdofprey(ip,api_name,oauth_token,oauth_token_secret)
        urlv.start()
        source.append(urlv)
        print ip

    for host in range(67,134):
        ## User 2 in API
        ip                  = data3[host]['screen_name']
        oauth_token         = data2[0][str(delta+1)]['oauth_token']
        oauth_token_secret  = data2[0][str(delta+1)]['oauth_token_secret']
        urlv                = birdofprey(ip,api_name,oauth_token,oauth_token_secret)
        urlv.start()
        source.append(urlv)
        print ip

    api_name2 = api_name + 1

    for host in range(134,168):
        ## User 3 in API
        ip                  = data3[host]['screen_name']
        oauth_token         = data2[0][str(delta+2)]['oauth_token']
        oauth_token_secret  = data2[0][str(delta+2)]['oauth_token_secret']
        urlv                = birdofprey(ip,api_name2,oauth_token,oauth_token_secret)
        urlv.start()
        source.append(urlv)
        print ip

    for host in range(168,194):
        ## User 3 in API
        ip                  = data3[host]['screen_name']
        oauth_token         = data2[0][str(delta+2)]['oauth_token']
        oauth_token_secret  = data2[0][str(delta+2)]['oauth_token_secret']
        urlv                = birdofprey(ip,api_name2,oauth_token,oauth_token_secret)
        urlv.start()
        source.append(urlv)
        print ip

    print "Complete"

## Timing Script

def time_code(arg):
    '''For running code once,and take time'''
    start       = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(lvl1)