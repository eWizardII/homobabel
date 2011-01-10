import time
import json
import string
import unicodedata
import os

def filetxt():
    word_freq = {}
    word_occ  = {}
    word_supp = {}
    word_stat = {}
    word_users_behind_word = {}
    lvl1      = []
    lvl2      = []
    total_t   = 0
    users     = 0
    text      = []
    foll      = []
    stat      = []
    word_list = []
    path="C:\Twitter\json_"
    dirList=os.listdir(path)

    print "Directory Listing Complete"
    errors = 0
    for fname in dirList:
        # Open File
        try:
            with open("C:/Twitter/json_/" + str(fname), "r") as f:
                text_f = json.load(f)
                stat_v = text_f['0']['statuses_count']
                foll_v = text_f['0']['followers_count']
                if (stat_v > 10) and (foll_v > 10):
                    users = users + 1
                    for i in range(len(text_f)):
                        text.append(text_f[str(i)]['text'])
                        stat.append(stat_v)
                        foll.append(foll_v)
                        total_t = total_t + 1
                else:
                    pass
        except:
            errors += errors
            pass
        
    print "Running Filter"

    # Filter
    occ = 0
    import string
    for i in range(len(text)):
        s = text[i] # Sample string
        occ_t = s.count('RT') + s.count('@')
        supp_t = foll[i]
        stat_t = stat[i]
        occ += occ_t
        s = s.encode('utf-8')
        out = s.translate(string.maketrans("",""), string.punctuation)

        # Create Wordlist/Dictionary
        word_lists = text[i].lower().split(None)
        for word in word_lists:
            word_freq[word] = word_freq.get(word, 0) + 1
            word_occ[word]  = word_occ.get(word, 0) + occ_t
            word_supp[word] = word_supp.get(word, 0) + supp_t
            word_stat[word] = word_stat.get(word, 0) + stat_t
            word_users_behind_word[word] = word_users_behind_word.get(word, 0) + 1 

    print "Running Analysis"
    
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

    ## Write data for analysis
    print "Saving Analysis"
    
    mo = open("matlab.txt", "wb")
    
    for row in word_occ:
        mo.write(str(row.encode('utf_8'))+" "+str(word_occ[row])+" "+str(word_supp[row]/word_users_behind_word[row])+" "+str(word_stat[row]/word_users_behind_word[row])+'\r\n')
        #mo.write(str(row.encode('utf_8'))+" "+str(word_occ[row])+'\r\n')

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
    print "Total Errors: " + str(errors)
    
    print "Done!"

def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)
    
if __name__ == '__main__':
    time_code(filetxt)
