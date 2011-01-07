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
import threading
from threading import Thread
from tweepy.cursor import Cursor



#Run main program
#Creates a thread of network calls to Twitter passes through VPN and Proxy


def lvl1():

    ## Thread loop - birdofprey

    class birdofprey(Thread):
        def __init__ (self,ip,id,api_name,oauth_token,oauth_token_secret):
            Thread.__init__(self)
            self.ip                 = ip
            self.id                 = id
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
            api.retry_count = 5
            api.retry_delay = 10


            ## Grab the seeds (i.e. the top 100 Twitter users ranging from @ladygaga - @womensweardaily

            j = 0
            for null in range(0,1):
                while True:
                    try:
                        with open('C:/Twitter/tweets/user_0_' + str(self.id) + '.json', mode='w') as f:
                            f.write('[')
                            threadLock.acquire()
                            for i, seed in enumerate(Cursor(api.user_timeline,screen_name=self.ip).items(200)):
                                if i>0:
                                    f.write(", ")
                                f.write("%s" % (json.dumps(dict(sc=seed.author.statuses_count))))
                                j = j + 1
                            threadLock.release()
                            f.write("]")
                    except tweepy.TweepError, e:
                        with open('C:/Twitter/tweets/user_0_' + str(self.id) + '.json', mode='a') as f:
                            f.write("]")
                        print "ERROR on " + str(self.ip) + " Reason: ", e
                        with open('C:/Twitter/errors_0.txt', mode='a') as a_file:
                            new_ii = "ERROR on " + str(self.ip) + " Reason: " + str(e) + "\n"
                            a_file.write(new_ii)
                    break


            ## Display the status of the project

            print str(j) + " tweets found for " + str(self.ip) + " \n"
            print "Completed"

            ## Log the status of the project

            with open('C:/Twitter/pre_status_0.txt', mode='a') as a_file:
                new_iii = str(j) + " tweets found for " + str(self.ip) + " \n"
                new_iv  = "Completed" + " \n"
                a_file.write(new_iii)
                a_file.write(new_iv)

        def join(self,timeout=None):
            Thread.join(self, timeout)

    ## Necessary Variables

    threadLock = threading.Lock()
    source      = []
    api_name    = 1
    json_data2  = open("C:/Twitter/commodore.json")
    data2       = json.load(json_data2)
    id          = -1

    json_data3  = open("C:/Twitter/top100.json")
    data3       = json.load(json_data3)

    ## Massive For-loop used to call the correct APIs and Twitter Users

    for host in range(0,75):
        ## User 1 in API
        ip                  = data3[host]['su']
        id                  = id + 1
        oauth_token         = data2[0]['oauth_token']
        oauth_token_secret  = data2[0]['oauth_token_secret']
        urlv                = birdofprey(ip,id,api_name,oauth_token,oauth_token_secret)
        urlv.start()
        source.append(urlv)
        #print ip

    for host in range(75,150):
        ## User 2 in API
        ip                  = data3[host]['su']
        id                  = id + 1
        oauth_token         = data2[1]['oauth_token']
        oauth_token_secret  = data2[1]['oauth_token_secret']
        urlv                = birdofprey(ip,id,api_name,oauth_token,oauth_token_secret)
        urlv.start()
        source.append(urlv)
        #print ip

    api_name2 = api_name + 1

    for host in range(150,188):
        ## User 3 in API
        ip                  = data3[host]['su']
        id                  = id + 1
        oauth_token         = data2[2]['oauth_token']
        oauth_token_secret  = data2[2]['oauth_token_secret']
        urlv                = birdofprey(ip,id,api_name2,oauth_token,oauth_token_secret)
        urlv.start()
        source.append(urlv)
        #print ip

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