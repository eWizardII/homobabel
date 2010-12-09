import os
import re
import time
import sys
from threading import Thread
import urllib2
import json
import gzip
import threading
import tweepy
import urlparse
import oauth2 as oauth
from datetime import datetime

def lvl1(min_i,max_i,api_name):
    
    storage_ii = 0
    blocked = 0
    allowed = 0
    
    class birdofprey(Thread):
        def __init__ (self,ip):
            Thread.__init__(self)
            self.ip = ip
            
        def run(self):
            try:

                '''OAuth Dance!'''
                consumer_key = 'TVjUUCHjcjRAQBzxNeqevQ'
                consumer_secret = 'uDs577RFeCePYEGnFSw0npvPuT6waStSO8UNz6L4'
                consumer = oauth.Consumer(consumer_key, consumer_secret)

                oauth_token = '125084643-t7NLHdd22fxrbQAqjZklaJIYkHhBadzIjhxPwHtp'
                oauth_token_secret = '9Trtl2zu0Zxx320InBzwYSUlDoFAVZjy1TmhvwlhZQ'
                token = oauth.Token(oauth_token, oauth_token_secret)
                client = oauth.Client(consumer, token)
                
                PROXY_DOMAIN = "twitter" + str(api_name) + "-ewizardii.apigee.com"
                pidgin = ("http://twitter" + str(api_name) + "-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(self.ip) + ".json?count=200&trim_user=true")
                resp, content = client.request(pidgin, "GET", PROXY_DOMAIN)
                output = str(content)
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
                self.passed = 1
                self.block = 0
            except:
                self.storage_i = 0
                self.block = 1
                self.passed = 0
        def join(self,timeout=None):
            Thread.join(self, timeout)
    
    ThreadLock = threading.Lock()        
    source = []
    storage_ii = 0
    blocked = 0
    allowed = 0
    
    for host in range(min_i,max_i):
        ip = str(host)
        urlv = birdofprey(ip)
        urlv.start()
        source.append(urlv)

    for threads in source:
        threads.join()
        storage_ii = threads.storage_i + storage_ii
        allowed = threads.passed + allowed
        blocked = threads.block + blocked
    print str(storage_ii) + ' ' + str(allowed) + ' ' + str(blocked)
    with open('B:/Twitter/log.txt', mode='a') as a_file:
        new_ii = str(storage_ii) + '\t A:' + str(allowed) + '\t B:' + str(blocked) + '\n'
        a_file.write(new_ii)
    
    for host in range(min_i,max_i):
        try:
            os.remove("B:/Twitter/json_scrap/temp_" + str(host) + ".json")
        except:
            pass
    
def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    start_time = str(datetime.now()) + '\n'
    alpha = 1
    intra = 20
    beta = alpha + 2*intra
    arg(alpha,alpha+intra,1)
    arg(alpha+intra,alpha+2*intra,2)
    arg(alpha+2*intra,alpha+3*intra,3)
    arg(alpha+3*intra,alpha+4*intra,4)
    arg(alpha+4*intra,alpha+5*intra,5)
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)
    end_time = str(datetime.now()) + '\n'
    with open('B:/Twitter/time.txt', mode='a') as a_file:
        new_ii = str(end - start) + '\n'
        header = "Starting with user_id: " + str(alpha) " and ending with user_id: " + str(beta)
        a.file.write(header)
        a_file.write(start_time)
        a_file.write(new_ii)
        a_file.write(end_time)

if __name__ == '__main__':
    time_code(lvl1)
