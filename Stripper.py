import time
import json
import string
import unicodedata
import os.path

def filetxt():
    word_freq = {}
    word_occ  = {}
    lvl1      = []
    lvl2      = []
    total_t   = 0
    users     = 0
    text      = []
    word_list = []
    
    for l in range(2500,234980613):
        # Open File
        if os.path.exists("C:/Twitter/json_/user_" + str(l) + "_id_" + str(l) + ".json") == True:
            with open("C:/Twitter/json_/user_" + str(l) + "_id_" + str(l) + ".json", "r") as f:
                text_f = json.load(f)
                users = users + 1
                for i in range(len(text_f)):
                    text.append(text_f[str(i)]['text'])
                    total_t = total_t + 1
        else:
            pass

    # Filter
    occ = 0
    import string
    for i in range(len(text)):
        s = text[i] # Sample string
        occ_t = s.count('RT') + s.count('@')
        occ += occ_t
        s = s.encode('utf-8')
        out = s.translate(string.maketrans("",""), string.punctuation)

        # Create Wordlist/Dictionary
        word_lists = text[i].lower().split(None)
        for word in word_lists:
            word_freq[word] = word_freq.get(word, 0) + 1
            word_occ[word]  = word_occ.get(word, 0) + occ_t
            
    keys = word_freq.keys()

    numbo = range(1,len(keys)+1)
    NList = str(numbo).strip('[]')
    WList = list(keys)
    NList = NList.split(", ")
    W2N = dict(zip(WList, NList))
    
    for i in range(len(text)):
        word_list = text[i].lower().split(None)
        
        for k in range (0,len(word_list)):
            word_list[k] = W2N[word_list[k]]
        for i in range (0,len(word_list)-1):
            lvl1.append(word_list[i])
            lvl2.append(word_list[i+1])

    out_f = open("matlab.txt", 'w')

    mo = open("matlab.txt", "wb")
    
    for row in word_occ:
        mo.write(str(row.encode('utf_8'))+" "+str(word_occ[row])+'\r\n')

    mo.close()
    
    # Write all to File
    fo = open("output.txt", "wb")

    # Print Vertices
    fo.write('*Vertices ' + str(len(keys)) + '\r\n')

    for i in range (0,len(keys)):
        j = i + 1
        fo.write(str(j)+" "+"\""+keys[i].encode('utf-8')+"\""+'\r\n')

    print "Done Vertices!"

    # Generate and Print the Edges
    fo.write('*Edges ' + '\r\n')

    for i in range (0,len(lvl1)-1):
        fo.write(lvl1[i]+" "+lvl2[i+1]+ '\r\n')
        
    print "Done Edges!"
    fo.close()

    print "Total Tweets: " + str(total_t)
    print "Total Users:  " + str(users)
    print "Total Occ: " + str(occ)
    
    print "Done!"

def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)
    
if __name__ == '__main__':
    time_code(filetxt)
