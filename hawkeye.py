#!/usr/bin/env python
"""
eagle_prefetch.py
Designed to scan Twitter for viable accounts, for established parameters
Selects the userd_ids of the top 100 followed and follower accounts

Solomon Abiola
http://www.ewizardii.com
"""

## Import Modules
from random import shuffle
import os
import time
from threading import Thread
import json
import gzip
import oauth2 as oauth

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

            consumer_key = '3y1428CJNYI3uqgW8oFcEA'
            consumer_secret = 'GPpj8e6jOVkecaxfb5GmgIvI8ObnqYzo80oXt8v3c'
            consumer = oauth.Consumer(consumer_key, consumer_secret)

            token = oauth.Token(self.oauth_token, self.oauth_token_secret)
            client = oauth.Client(consumer, token)
            PROXY_DOMAIN = "twitter" + str(self.api_name) + "-ewizardii.apigee.com"

            try:
                pidgin = ("http://twitter" + str(self.api_name) + "-ewizardii.apigee.com/1/statuses/user_timeline.json?user_id="+ str(self.ip) + "?count=200")
                resp, content = client.request(pidgin, "GET", PROXY_DOMAIN)
                output = str(content)
                fileObj = open("C:/Twitter/json_scrap/temp_" + str(self.ip) + ".json","w")
                fileObj.write(output)
                fileObj.close()

                ## Grab the tweets per user

                ## Create scratch for JSON file
                json_data = open("C:/Twitter/json_scrap/temp_" + str(self.ip) + ".json")
                data = json.load(json_data)

                ## Get selected data from JSON file

                i = 0
                twitter_data = {}
                for record in data:
                    twitter_data[i]                                 = {}
                    twitter_data[i]['created_at']                   = data[i]['created_at']
                    twitter_data[i]['favorited']                    = data[i]['favorited']
                    twitter_data[i]['id_str']                       = data[i]['id_str']
                    twitter_data[i]['in_reply_to_status_id_str']    = data[i]['in_reply_to_status_id_str']
                    twitter_data[i]['in_reply_to_user_id_str']      = data[i]['in_reply_to_user_id_str']
                    twitter_data[i]['retweet_count']                = data[i]['retweet_count']
                    twitter_data[i]['retweeted']                    = data[i]['retweeted']
                    twitter_data[i]['text']                         = data[i]['text']
                    record_id                                       = data[i]['user']
                    twitter_data[i]['id_str']                       = record_id['id_str']
                    twitter_data[i]['id']                           = record_id['id']
                    twitter_data[i]['location']                     = record_id['location']
                    twitter_data[i]['time_zone']                    = record_id['time_zone']
                    twitter_data[i]['followers_count']              = record_id['followers_count']
                    twitter_data[i]['created_at']                   = record_id['created_at']
                    twitter_data[i]['statuses_count']               = record_id['statuses_count']
                    twitter_data[i]['verified']                     = record_id['verified']
                    twitter_data[i]['screen_name']                  = record_id['screen_name']
                    i = i + 1

                ## Write JSON and compress it into Gzip

                with open('C:/Twitter/json/user_' + str(self.ip) + '_id_' + str(record_id['id_str'])+ '.json', mode='w') as f:
                    json.dump(twitter_data, f, indent=2, encoding='utf-8')

#                f_in = open('C:/Twitter/json/user_' + str(self.ip) + '_id_' + str(record_id['id_str'])+ '.json', 'rb')
#                f_out = gzip.open('C:/Twitter/json/user_' + str(self.ip) + '_id_' + str(record_id['id_str'])+ '.json.gz', 'wb')
#                f_out.writelines(f_in)
#                f_out.close()
#                f_in.close()
#                os.remove('C:/Twitter/json_scrap/temp_" + str(self.ip) + ".json')
                self.storage_i = i
                self.passed = 1
                self.block = 0

                ## Display the status of the project

                ## print str(i) + " tweets found for " + str(self.ip) + " \n"
                ## print "Completed"

                ## Log the status of the project

                with open('C:/Twitter/status.txt', mode='a') as a_file:
                    new_iii = str(i) + " tweets found for " + str(self.ip) + " \n"
                    a_file.write(new_iii)
                    a_file.write(new_iv)
            except:
                pass
#                with open('C:/Twitter/error_log.txt', mode='a') as a_file:
#                    new_i = str(self.ip) + '\t R:' + str(content) + '\n'
#                    a_file.write(new_i)


        def join(self,timeout=None):
            Thread.join(self, timeout)

    ## Necessary Variables

    source      = []
    json_data2  = open("C:/Twitter/commodore.json")
    data2       = json.load(json_data2)
    id          = -1
    ## In manual mode you will want to set this k
    k           = 0

    ## Load the Users into the RAM

    a = set()
    for i in range(1):
        with open("C:/Twitter/user/user_{0}.json".format(i)) as json_data:
            data = json.load(json_data)
            a.update(d['su'] for d in data)

    print("Cleaned length is {0}".format(len(a)))

    # Take Cleaned List and Randomize it for Analysis
    new = list(a)
    shuffle(new)

    # Delete old Arrays to clear up RAM
    del a
    del data

    ## Massive For-loop used to call the correct APIs and Twitter Users
    for hour in range(3):
        for host in range(0,9750):
            ## User 1 and 2 in API 1
            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[0]['oauth_token']
            oauth_token_secret  = data2[0]['oauth_token_secret']
            urlv                = birdofprey(ip,id,1,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[1]['oauth_token']
            oauth_token_secret  = data2[1]['oauth_token_secret']
            urlv                = birdofprey(ip,id,1,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

            ## User 3 in API 1
            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[2]['oauth_token']
            oauth_token_secret  = data2[2]['oauth_token_secret']
            urlv                = birdofprey(ip,id,1,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[0]['oauth_token']
            oauth_token_secret  = data2[0]['oauth_token_secret']
            urlv                = birdofprey(ip,id,2,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

            ## User 3 in API 2
            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[1]['oauth_token']
            oauth_token_secret  = data2[1]['oauth_token_secret']
            urlv                = birdofprey(ip,id,2,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

            ## User 3 in API 2
            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[2]['oauth_token']
            oauth_token_secret  = data2[2]['oauth_token_secret']
            urlv                = birdofprey(ip,id,2,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

        for host in range(0,9750):

            ## User 1 and 2 in API 1
            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[0]['oauth_token']
            oauth_token_secret  = data2[0]['oauth_token_secret']
            urlv                = birdofprey(ip,id,1,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[1]['oauth_token']
            oauth_token_secret  = data2[1]['oauth_token_secret']
            urlv                = birdofprey(ip,id,1,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

            ## User 1 and 2 in API 2
            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[0]['oauth_token']
            oauth_token_secret  = data2[0]['oauth_token_secret']
            urlv                = birdofprey(ip,id,2,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

            ip                  = new[k]
            id                  = id + 1
            oauth_token         = data2[1]['oauth_token']
            oauth_token_secret  = data2[1]['oauth_token_secret']
            urlv                = birdofprey(ip,id,2,oauth_token,oauth_token_secret)
            urlv.start()
            source.append(urlv)
            k                   = k + 1

        time.sleep(4200)

        print "Done Sleeping"
    
        print "Complete Hour: " + str(hour)

## Timing Script

def time_code(arg):
    '''For running code once,and take time'''
    start       = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(lvl1)