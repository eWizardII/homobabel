import time

def filetxt():
    # Open File
    file = open("kjv12.txt", "r")
    text = file.read()
    text = text + text + text + text + text + text + text + text + text + text + text + text
    file.close()

    # Filter


    import string
    s = text # Sample string 
    out = s.translate(string.maketrans("",""), string.punctuation)


    # Create Wordlist/Dictionary
    word_list = text.lower().split(None)
    word_freq = {}

    for word in word_list:
        word_freq[word] = word_freq.get(word, 0) + 1
        
    keys = sorted(word_freq.keys())


    # Write all to File
    fo = open("output.txt", "wb")

    # Print Vertices
    fo.write('*Vertices ' + str(len(keys)) + '\r\n')

    for i in range (0,len(keys)):
        j = i + 1
        fo.write(str(j)+" "+"\""+keys[i]+"\""+'\r\n')

    print "Done Vertices!"

    # Generate and Print the Edges
    fo.write('*Edges ' + '\r\n')
    import string
    numbo = range(1,len(keys)+1)
    WList = ', '.join(keys)
    NList = str(numbo).strip('[]')
    WList = WList.split(", ")
    NList = NList.split(", ")
    W2N = dict(zip(WList, NList))

    for k in range (0,len(word_list)):
        word_list[k] = W2N[word_list[k]]

    #fo.write('*Edges' + '\r\n')
    for i in range (0,len(word_list)-1):
        fo.write(word_list[i]+" "+word_list[i+1]+ '\r\n')
        
    print "Done Edges!"
    fo.close()
    print "Done!"

def time_code(arg):
    '''For running code once,and take time'''
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)
    
if __name__ == '__main__':
    time_code(filetxt)
