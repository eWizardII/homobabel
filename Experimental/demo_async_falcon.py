import os
import re
import time
import sys
from threading import Thread
import urllib2
from BeautifulSoup import BeautifulSoup
import json
import gzip
import os
import threading

def lvl1():
    storage_ii = 0
    class birdofprey(Thread):
        def __init__ (self,ip):
            Thread.__init__(self)
            self.ip = ip
        def run(self):
            ThreadLock.acquire()
            try:
                pidgin = ("http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(ip) + ".json?count=200&trim_user=true")
                pidgin2 = urllib2.urlopen(pidgin) 
                soup = BeautifulSoup(pidgin2)
                output = str(soup)
                
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
                with open('B:/Twitter/json/' + str(record_id['id_str']) + '.json', mode='w') as f:
                    json.dump(twitter_data, f, indent=2, encoding='utf-8')
                f_in = open('B:/Twitter/json/' + str(record_id['id_str']) + '.json', 'rb')
                f_out = gzip.open('B:/Twitter/json/' + str(record_id['id_str']) + '.json.gz', 'wb')
                f_out.writelines(f_in)
                f_out.close()
                f_in.close()
                os.remove('B:/Twitter/json/' + str(record_id['id_str']) + '.json')
                self.storage_i = i
            except:
                self.storage_i = 0
            ThreadLock.release()
        def join(self,timeout=None):
            Thread.join(self, timeout)
            

    ThreadLock = threading.Lock()        
    source = []
    storage_ii = 0
    
    for host in range(1,10):
        ip = str(host)
        urlv = birdofprey(ip)
        urlv.start()
        urlv.join()
        storage_ii = urlv.storage_i + storage_ii
        print "Active: " + str(threading.activeCount())
    print str(storage_ii)

def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(lvl1)
