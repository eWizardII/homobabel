import time
import json
import gzip
from pprint import pprint
import urllib2
from time import sleep
from BeautifulSoup import BeautifulSoup
import os

def norris():
    tu = 0
    su = 0
    ou = 0
    i  = 1
    for j in range (1,20):
        try:
            urlv = "http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i) + ".json?count=200&trim_user=true"
            source = urllib2.urlopen(urlv)
            urlv2 = "http://twitter2-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i+1) + ".json?count=200&trim_user=true"
            source2 = urllib2.urlopen(urlv2)
            urlv3 = "http://twitter3-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i+2) + ".json?count=200&trim_user=true"
            source3 = urllib2.urlopen(urlv3)
            urlv4 = "http://twitter4-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i+3) + ".json?count=200&trim_user=true"
            source4 = urllib2.urlopen(urlv4)
            urlv5 = "http://twitter5-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i+4) + ".json?count=200&trim_user=true"
            source5 = urllib2.urlopen(urlv5)
            i = i + 5
##            soup = BeautifulSoup(source)
##            output = str(soup)
##
##            fileObj = open("/media/Cache/Twitter/json_scrap/temp.json","w")
##            fileObj.write(output)
##            fileObj.close()
##
##            json_data = open("/media/Cache/Twitter/json_scrap/temp.json")
##
##            data = json.load(json_data)
##
##            i = 0
##            twitter_data = {}
##            for record in data:
##                twitter_data[i]                                 = {}
##                twitter_data[i]['created_at']                   = record['created_at']
##                twitter_data[i]['favorited']                    = record['favorited']
##                twitter_data[i]['id_str']                       = record['id_str']
##                twitter_data[i]['in_reply_to_status_id_str']    = record['in_reply_to_status_id_str']
##                twitter_data[i]['in_reply_to_user_id_str']      = record['in_reply_to_user_id_str']
##                twitter_data[i]['retweet_count']                = record['retweet_count']
##                twitter_data[i]['retweeted']                    = record['retweeted']
##                twitter_data[i]['text']                         = record['text']
##                twitter_data[i]['user']                         = record['user']
##                record_id                                       = record['user']
##                twitter_data[i]['id_str']                       = record_id['id_str']
##                i = i + 1
##
##            with open('/media/Cache/Twitter/junk/' + str(record_id['id_str']) + '.json', mode='w') as f:
##                json.dump(twitter_data, f, indent=2, encoding='utf-8')
##
##            f_in = open('/media/Cache/Twitter/junk/' + str(record_id['id_str']) + '.json', 'rb')
##            f_out = gzip.open('/media/Cache/Twitter/junk/' + str(record_id['id_str']) + '.json.gz', 'wb')
##            f_out.writelines(f_in)
##            f_out.close()
##            f_in.close()
##            os.remove('/media/Cache/Twitter/junk/' + str(record_id['id_str']) + '.json')
            ou = ou + 1
            tu = tu + 1
        except:
            su = su + 1
            tu = tu + 1

def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(norris)
