#!/usr/bin/env python
"""
hawkeye.py
Designed to scan Twitter for viable accounts, for established parameters

Solomon Abiola
http://www.ewizardii.com
"""

## Import Modules
import os
import re
import time
import urllib2
import json
import gzip
import threading
import urlparse
import tweepy
from threading import Thread
from datetime import datetime
from time import gmtime, strftime
from UserString import MutableString

"""
Run main program
Creates a thread of network calls to Twitter
"""

def lvl1(min_i,max_i):

    ## Thread loop - birdofprey
    
    class birdofprey(Thread):
        def __init__ (self,ip,api_name,oauth_token,oauth_token_secret):
            Thread.__init__(self)
            self.ip = ip
            self.api_name = api_name
            
        def run(self):
            try:

            ## OAuth Dance!
            
                CONSUMER_KEY = '3y1428CJNYI3uqgW8oFcEA'
                CONSUMER_SECRET = 'GPpj8e6jOVkecaxfb5GmgIvI8ObnqYzo80oXt8v3c'

                
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                api = tweepy.API(auth)

                """
                Create Custom JSON file, ignore any errors, such as those that might be generated by a 401
                """

                data = api.lookup_users(self.ip)
                data_ = data
                    
                i = 0
                twitter_data = {}
                for record in data:
                    data_                                           = data[i]
                    twitter_data[i]                                 = {}
                    twitter_data[i]['statuses_count']               = data_.statuses_count
                    twitter_data[i]['lang']                         = data_.lang
                    twitter_data[i]['id_str']                       = data_.id_str
                    twitter_data[i]['screen_name']                  = data_.screen_name
                    twitter_data[i]['followers_count']              = data_.followers_count
                    twitter_data[i]['verified']                     = data_.verified
                    twitter_data[i]['friends_count']                = data_.followers_count
                    twitter_data[i]['protected']                    = data_.protected
                    twitter_data[i]['created_at']                   = data_.created_at.strftime("[%d/%b/%Y:%H:%M:%S +0000]")

                    size_ = data_.statuses_count * 100
                    
                    if data_.protected == True :
                        status = '401'
                        with open('B:/Twitter/block.txt', mode='a') as a_file:
                            new_v = str(str(data_.statuses_count) + '\n')
                            a_file.write(new_v)
                    else:
                        status = '200'
                        with open('B:/Twitter/allow.txt', mode='a') as a_file:
                            new_iv = str(str(data_.statuses_count) + '\n')
                            a_file.write(new_iv)
                        
                    with open('B:/Twitter/network.log', mode='a') as a_file:
                        new_iii = str("Thread:" + str(i)) + " " + "-" + " "+ "-" + " " + str(strftime("[%d/%b/%Y:%H:%M:%S +0000]", gmtime())) + " " + "\"GET /1/users/lookup.json?user_id=" +  str(data_.id_str) + " HTTP/1.1\"" + " " + str(status) + " " + str(size_) + " " + "\"-\"" + " " + "\"-\"" + " " + "\"-\"" + '\n'
                        a_file.write(new_iii)
                    i = i + 1

                with open('B:/Twitter/json/user_' + str(data_.id_str) + '.json', mode='w') as f:
                    json.dump(twitter_data, f, indent=2, encoding='utf-8')
                
            except:
                ##print Exception
                pass
            
        def join(self,timeout=None):
            Thread.join(self, timeout)

    """
    Neccesary Variables
    """
    
    ThreadLock = threading.Lock()        
    source = []
    A_ = 0
    delta = 0
    api_name = 1
    json_data2 = open("B:/Twitter/commodore.json")
    data2 = json.load(json_data2)
    start = 19500

    ## Generate User List
    
    str_list = []
    for num in xrange(min_i,max_i):
        str_list.append(`num`)

    ITER = max_i/100

    """
    Massive For-loop used to call the correct APIs and Twitter Users
    """
    
    for host in range(0,ITER):

            for eye in range(0,1):
                ## User 1 in First API
                ##BLOCK = ','.join(str_list[A_:A_+100])
                ip = str_list[A_:A_+100]
                oauth_token = data2[0][str(delta)]['oauth_token']
                oauth_token_secret = data2[0][str(delta)]['oauth_token_secret']
                urlv = birdofprey(ip,api_name,oauth_token,oauth_token_secret)
                urlv.start()
                source.append(urlv)
##                
##                ## User 2 in First API
##                BLOCK = ','.join(str_list[A_+100:A_+200])
##                ip = str(BLOCK)
##                oauth_token = data2[0][str(delta+1)]['oauth_token']
##                oauth_token_secret = data2[0][str(delta+1)]['oauth_token_secret']
##                urlv = birdofprey(ip,api_delta,oauth_token,oauth_token_secret)
##                urlv.start()
##                source.append(urlv)

            A_ = A_ + 100

##            ## Define Second API
##
##            api_delta2 = api_delta + 1
##
##            for eye2 in range(0,9750):
##                ## User 3.0 in First API
##                BLOCK = ','.join(str_list[A_:A_+100])
##                ip = str(BLOCK)
##                oauth_token = data2[0][str(delta+2)]['oauth_token']
##                oauth_token_secret = data2[0][str(delta+2)]['oauth_token_secret']
##                urlv = birdofprey(ip,api_delta,oauth_token,oauth_token_secret)
##                urlv.start()
##                source.append(urlv)
##
##                ## User 3.5 in Second API
##                BLOCK = ','.join(str_list[A_+100:A_+200])
##                ip = str(BLOCK)
##                oauth_token = data2[0][str(delta+2)]['oauth_token']
##                oauth_token_secret = data2[0][str(delta+2)]['oauth_token_secret']
##                urlv = birdofprey(ip,api_delta2,oauth_token,oauth_token_secret)
##                urlv.start()
##                source.append(urlv)                
##                
##                A_ = A_ + 200
##
##            for eye3 in range(0,19500):
##                ## User 1 in Second API
##                BLOCK = ','.join(str_list[A_:A_+100])
##                ip = str(BLOCK)
##                oauth_token = data2[0][str(delta)]['oauth_token']
##                oauth_token_secret = data2[0][str(delta)]['oauth_token_secret']
##                urlv = birdofprey(ip,api_delta2,oauth_token,oauth_token_secret)
##                urlv.start()
##                source.append(urlv)
##
##                ## User 2 in Second API
##                BLOCK = ','.join(str_list[A_+100:A_+200])
##                ip = str(BLOCK)
##                oauth_token = data2[0][str(delta+1)]['oauth_token']
##                oauth_token_secret = data2[0][str(delta+1)]['oauth_token_secret']
##                urlv = birdofprey(ip,api_delta2,oauth_token,oauth_token_secret)
##                urlv.start()
##                source.append(urlv)
##                
##                A_ = A_ + 200
    
##            delta = delta + 3
##            api_delta = api_delta + 2
            print "Restarting"

''' Timing Script '''
    
def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    start_time = str(datetime.now()) + '\n'
    alpha = 1
    beta = 1000
    arg(alpha,beta)
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)
    end_time = str(datetime.now()) + '\n'
    with open('B:/Twitter/time.txt', mode='a') as a_file:
        new_ii = str(end - start) + '\n'
        header = "Starting with user_id: " + str(alpha) + " and ending with user_id: " + str(beta) + '\n'
        a_file.write(header)
        a_file.write(start_time)
        a_file.write(new_ii)
        a_file.write(end_time)

if __name__ == '__main__':
    time_code(lvl1)
