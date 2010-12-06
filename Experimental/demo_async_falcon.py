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

def lvl1(min_i,max_i,api):
    storage_ii = 0
    class birdofprey(Thread):
        def __init__ (self,ip):
            Thread.__init__(self)
            self.ip = ip
        def run(self):
            try:
                pidgin = ("http://twitter" + str(api) + "-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(self.ip) + ".json?count=200&trim_user=true")
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
    
    for host in range(min_i,max_i):
        try:
            os.remove("B:/Twitter/json_scrap/temp_" + str(host) + ".json")
        except:
            pass
    
def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    alpha = 20000
    arg(alpha,alpha+20000,1)
    arg(alpha+20000,alpha+40000,2)
    arg(alpha+40000,alpha+60000,3)
    arg(alpha+80000,alpha+100000,4)
    arg(alpha+100000,alpha+120000,5)
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(lvl1)
