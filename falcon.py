import urllib2
import time
def norris():
    j = 1
    source = {}
    while (j < 100):
        try:
            class MyHttpHandler(urllib2.HTTPHandler):
                def http_response(self, request, response):
                    return response

            u = urllib2.build_opener(MyHttpHandler())
            for i in range(j, 100):
                source[i] = u.open("http://twitter1-ewizardii.apigee.com/1/statuses/user_timeline/"+ str(i) + ".json?count=200&trim_user=true")
                j = j + 1
        except:
            j = j + 1
def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

if __name__ == '__main__':
    time_code(norris)
