print "Welcome to Word Frequency Sorter!!\n"

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

filenames = ['Kaplan.txt','Magoosh.txt','Manhattan.txt','Barrons.txt','Princeton.txt','Majortest.txt']
with open('allwords.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                line =line.lower()
                outfile.write(line)

with open("allwords.txt") as f:
    items = f.readlines()
    t = items
    t = map(lambda items: items.strip(), t)
    for i, w in enumerate(t):
        t[i]=w.split(":", 1)[0]

l = open("output.txt","w").close()
l = open("output.txt","a")
l.write("Most Frequent Words: \n")

for key, value in sorted(wordListToFreqDict(t).iteritems(), key=lambda (k,v): (v,k),reverse =True):
    l.write(" \n%s: %s" % (key, value))
l.close()
