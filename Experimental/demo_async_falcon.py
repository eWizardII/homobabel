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
    class birdofprey(Thread):
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
                    
            except:
                pass
               
    source = []

    for host in range(1,100):
       ip = str(host)
       urlv = birdofprey(ip)
       urlv.start()

def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(lvl1)
