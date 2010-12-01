import urllib2
from time import sleep
from BeautifulSoup import BeautifulSoup
b = 1
for j in range (1,2000):
    for i in range (1,2):
        print "Bacth " + str(i)
        urlv = str()
        for a in range (115487,116487):
            urlv = urlv + str(a) + ","
        else:
            urlv = urlv + str(a+1)
            print "Batch of users ending in " + str(a+1)
        urlv = "https://graph.facebook.com/?ids=" + urlv + "&fields=feed&since=2010-10-01&until=2010-11-01&limit=500&format=json"
        source = urllib2.urlopen(urlv)
        soup = BeautifulSoup(source)
        output = str(soup)
        fileObj = open("C:/TEMP/part" + str(a) + ".txt","w")
        fileObj.write(output)
        fileObj.close()
        b = b + 2
    for k in range (1,2):
        sleep(3)
        print "Sleeping for " + str(180-k) + " seconds"
    else:
        print "Waking up..."
else:
    print "Batch rounds of " + str(j) + " completed..."
