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

numo_t = []
for numo in range(1,7):
    pidgin = ("http://twitter" + str(numo) + "-ewizardii.apigee.com/1/account/rate_limit_status.json")
    pidgin2 = urllib2.urlopen(pidgin) 
    soup = BeautifulSoup(pidgin2)
    output = str(soup)
    fileObj = open("B:/Twitter/json_scrap/api_" + str(numo) + ".json","w")
    fileObj.write(output)
    fileObj.close()
    json_data = open("B:/Twitter/json_scrap/api_" + str(numo) + ".json")
    data = json.load(json_data)
    numo_t.append(data['remaining_hits'])
print numo_t
##if numo_t[0] < 1000:
##    api = 2
##elif numo_t[1] < 1000:
##    api = 3
##elif numo_t[2] < 1000:
##    api = 4
##elif numo_t[3] < 1000:
##    api = 5
##elif numo_t[4] < 1000:
##    print ("failure")
##    time.sleep(900)
##else:
##    api = 1
