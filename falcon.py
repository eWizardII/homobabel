import threading
from time import sleep
import urllib2
import time

def lvl1():
    j = 1
    source = {}
    while (j < 25):
        try:
            class MyHttpHandler(urllib2.HTTPHandler):
                def http_response(self, request, response):
                    return response

            u = urllib2.build_opener(MyHttpHandler())
            for i in range(j, 25):
                source[i] = u.open("http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i) + ".json?count=200&trim_user=true")
                j = j + 1
        except:
            j = j + 1

def lvl2():
    j = 1
    source = {}
    while (j < 25):
        try:
            class MyHttpHandler(urllib2.HTTPHandler):
                def http_response(self, request, response):
                    return response

            u = urllib2.build_opener(MyHttpHandler())
            for i in range(j, 25):
                source[i] = u.open("http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i) + ".json?count=200&trim_user=true")
                j = j + 1
        except:
            j = j + 1 

def lvl3():
    j = 1
    source = {}
    while (j < 25):
        try:
            class MyHttpHandler(urllib2.HTTPHandler):
                def http_response(self, request, response):
                    return response

            u = urllib2.build_opener(MyHttpHandler())
            for i in range(j, 25):
                source[i] = u.open("http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i) + ".json?count=200&trim_user=true")
                j = j + 1
        except:
            j = j + 1

def lvl4():
    j = 1
    source = {}
    while (j < 25):
        try:
            class MyHttpHandler(urllib2.HTTPHandler):
                def http_response(self, request, response):
                    return response

            u = urllib2.build_opener(MyHttpHandler())
            for i in range(j, 25):
                source[i] = u.open("http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i) + ".json?count=200&trim_user=true")
                j = j + 1
        except:
            j = j + 1
            
threading.Thread(target=lvl1).start()
threading.Thread(target=lvl2).start()
threading.Thread(target=lvl3).start()
threading.Thread(target=lvl4).start()

def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(lvl1)
    time_code(lvl2)
    time_code(lvl3)
    time_code(lvl4)
