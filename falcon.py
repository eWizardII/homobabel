import os
import re
import time
import sys
from threading import Thread
import urllib2
from BeautifulSoup import BeautifulSoup
import json
import gzip
import threading
import tweepy

CONSUMER_KEY = 'TVjUUCHjcjRAQBzxNeqevQ'
CONSUMER_SECRET = 'uDs577RFeCePYEGnFSw0npvPuT6waStSO8UNz6L4'
ACCESS_KEY = '125084643-t7NLHdd22fxrbQAqjZklaJIYkHhBadzIjhxPwHtp'
ACCESS_SECRET = '9Trtl2zu0Zxx320InBzwYSUlDoFAVZjy1TmhvwlhZQ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status("FALCON.PY initialized and transmitting to Twitter via homobabel-cmd")

def lvl1(min_i,max_i,api_name):
    storage_ii = 0
    class birdofprey(Thread):
        def __init__ (self,ip):
            Thread.__init__(self)
            self.ip = ip
        def run(self):
            try:
                pidgin = ("http://twitter" + str(api_name) + "-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(self.ip) + ".json?count=200&trim_user=true")
                pidgin2 = urllib2.urlopen(pidgin) 
                soup = BeautifulSoup(pidgin2)
                output = str(soup)
                ##print output
                fileObj = open("B:/Twitter/json_scrap/temp_" + str(self.ip) + ".json","w")
                fileObj.write(output)
                fileObj.close()

                json_data = open("B:/Twitter/json_scrap/temp_" + str(self.ip) + ".json")

                data = json.load(json_data)
                
                i = 0
                twitter_data = {}
                for record in data:
                    twitter_data[i]                                 = {}
                    twitter_data[i]['created_at']                   = record['created_at']
                    twitter_data[i]['favorited']                    = record['favorited']
                    twitter_data[i]['id_str']                       = record['id_str']
                    twitter_data[i]['in_reply_to_status_id_str']    = record['in_reply_to_status_id_str']
                    twitter_data[i]['in_reply_to_user_id_str']      = record['in_reply_to_user_id_str']
                    twitter_data[i]['retweet_count']                = record['retweet_count']
                    twitter_data[i]['retweeted']                    = record['retweeted']
                    twitter_data[i]['text']                         = record['text']
                    twitter_data[i]['user']                         = record['user']
                    record_id                                       = record['user']
                    twitter_data[i]['id_str']                       = record_id['id_str']
                    i = i + 1
                with open('B:/Twitter/json/user_' + str(self.ip) + '_id_' + str(record_id['id_str'])+ '.json', mode='w') as f:
                    json.dump(twitter_data, f, indent=2, encoding='utf-8')
                f_in = open('B:/Twitter/json/user_' + str(self.ip) + '_id_' + str(record_id['id_str'])+ '.json', 'rb')
                f_out = gzip.open('B:/Twitter/json/user_' + str(self.ip) + '_id_' + str(record_id['id_str'])+ '.json.gz', 'wb')
                f_out.writelines(f_in)
                f_out.close()
                f_in.close()
                os.remove('B:/Twitter/json/user_' + str(self.ip) + '_id_' + str(record_id['id_str'])+ '.json')
                self.storage_i = i
            except:
                self.storage_i = 0
        def join(self,timeout=None):
            Thread.join(self, timeout)
    
    ThreadLock = threading.Lock()        
    source = []
    storage_ii = 0
    
    for host in range(min_i,max_i):
        ip = str(host)
        urlv = birdofprey(ip)
        urlv.start()
        ##print "Active: " + str(threading.activeCount())
        source.append(urlv)

    for threads in source:
        threads.join()
        storage_ii = threads.storage_i + storage_ii
    print str(storage_ii)
    CONSUMER_KEY = 'TVjUUCHjcjRAQBzxNeqevQ'
    CONSUMER_SECRET = 'uDs577RFeCePYEGnFSw0npvPuT6waStSO8UNz6L4'
    ACCESS_KEY = '125084643-t7NLHdd22fxrbQAqjZklaJIYkHhBadzIjhxPwHtp'
    ACCESS_SECRET = '9Trtl2zu0Zxx320InBzwYSUlDoFAVZjy1TmhvwlhZQ'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status("Twitter" + str(api_name) + " API has collected: " + str(storage_ii) + " tweets!")
    
    for host in range(min_i,max_i):
        try:
            os.remove("B:/Twitter/json_scrap/temp_" + str(host) + ".json")
        except:
            pass
    
def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    alpha = 138400
    intra = 18000
    beta = alpha + 2*intra
    api.update_status("User: " + str(alpha)+ " ending with user " + str(beta))
    arg(alpha,alpha+intra,1)
    arg(alpha+intra,alpha+2*intra,2)
##    arg(alpha+2*intra,alpha+3*intra,3)
##    arg(alpha+3*intra,alpha+4*intra,4)
##    arg(alpha+4*intra,alpha+5*intra,5)
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)
    api.update_status("Complete Resting...")

if __name__ == '__main__':
    time_code(lvl1)
