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

def lvl1():
    storage_ii = 0
    class birdofprey(Thread):
        storage_i = 0
        def __init__ (self,ip):
            Thread.__init__(self)
            self.ip = ip
            self.status = -1
        def run(self):
            try:
                class MyHttpHandler(urllib2.HTTPHandler):
                    def http_response(self, request, response):
                        return response
            
                u = urllib2.build_opener(MyHttpHandler())
                pidgin = u.open("http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(ip) + ".json?count=200&trim_user=true")

                soup = BeautifulSoup(pidgin)
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
                with open('B:/Twitter/junk/' + str(record_id['id_str']) + '.json', mode='w') as f:
                    json.dump(twitter_data, f, indent=2, encoding='utf-8')
                f_in = open('B:/Twitter/junk/' + str(record_id['id_str']) + '.json', 'rb')
                f_out = gzip.open('B:/Twitter/junk/' + str(record_id['id_str']) + '.json.gz', 'wb')
                f_out.writelines(f_in)
                f_out.close()
                f_in.close()
                os.remove('B:/Twitter/junk/' + str(record_id['id_str']) + '.json')
                global storage_i
                storage_i = i      
            except:
                pass
            
    source = []
    
    for host in range(1,10):
        ip = str(host)
        urlv = birdofprey(ip)
        urlv.start()
        storage_ii = stroage_i + storage_ii
        print storage_ii

def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(lvl1)
