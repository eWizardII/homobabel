import time
import json
import gzip
from pprint import pprint
import urllib2
from time import sleep
from BeautifulSoup import BeautifulSoup
import os
tu = 0
su = 0
ou = 0
for j in range (inputs[job],inputs[job]+24):
    try:
        urlv = "http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(j) + ".json?count=200&trim_user=true"
        source = urllib2.urlopen(urlv)
        soup = BeautifulSoup(source)
        output = str(soup)

        fileObj = open("/media/Cache/Twitter/json_scrap/temp.json","w")
        fileObj.write(output)
        fileObj.close()

        json_data = open("/media/Cache/Twitter/json_scrap/temp.json")

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

        with open('/media/Cache/Twitter/junk/' + str(record_id['id_str']) + '.json', mode='w') as f:
            json.dump(twitter_data, f, indent=2, encoding='utf-8')

        f_in = open('/media/Cache/Twitter/junk/' + str(record_id['id_str']) + '.json', 'rb')
        f_out = gzip.open('/media/Cache/Twitter/junk/' + str(record_id['id_str']) + '.json.gz', 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        os.remove('/media/Cache/Twitter/junk/' + str(record_id['id_str']) + '.json')
        ou = ou + 1
        tu = tu + 1
    except:
        su = su + 1
        tu = tu + 1
