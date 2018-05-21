"""
Python Code to find out most frequent words from famous GRE lists

WordLists ( Courtesy: www.quizlet.com )
1. Barrons 1100 Words
2. Magoosh 1000 Words
3. Majortest Essential 1500 Words
4. Princeton 500 Words
5. Kaplan 500 Words
6. Manhattan Basic+Essential 1000 Words

Above words are stored in different text files along with definations. These text files are combined, parsed and word frequecy is calculated.
Word along with Frequenices is stored in output text file 'output.txt'
"""

print "Welcome to Word Frequency Sorter!!\n"

# Function to calculate word Frequency and store it into Dictionary
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

# Combine all wordslist text files into one and convert to lowercase.
filenames = ['Kaplan.txt','Magoosh.txt','Manhattan.txt','Barrons.txt','Princeton.txt','Majortest.txt']
with open('allwords.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                line =line.lower()
                outfile.write(line)

# Open combined wordlist, remove definations and format words
with open("allwords.txt") as f:
    items = f.readlines()
    t = items
    t = map(lambda items: items.strip(), t)
    for i, w in enumerate(t):
        t[i]=w.split(":", 1)[0]

#Clear contents of output text file.
l = open("output.txt","w").close()

#Open file and write sorted dictionary values into text file one by one in decreasing order
l = open("output.txt","a")
l.write("Most Frequent Words: \n")
for key, value in sorted(wordListToFreqDict(t).iteritems(), key=lambda (k,v): (v,k),reverse =True):
    l.write(" \n%s: %s" % (key, value))
l.close()
