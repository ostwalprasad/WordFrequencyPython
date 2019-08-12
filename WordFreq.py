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
from collections import defaultdict

# Function to calculate word Frequency and store it into Dictionary
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

# Combine all wordslist text files into one and convert to lowercase.
filenames = ['WordLists/Kaplan.txt','WordLists/Magoosh.txt','WordLists/Manhattan.txt','WordLists/Barrons.txt','WordLists/Princeton.txt','WordLists/Majortest.txt']
with open('CombinedAllWords.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname, encoding="ISO-8859-1") as infile:
            for line in infile:
                line = line.lower()
                outfile.write(line)

# Open combined wordlist, remove definations and format words
with open("CombinedAllWords.txt") as f:
    items = f.readlines()
    combined_vocab = items
    combined_vocab = list(map(lambda items: items.strip(), combined_vocab))
    for i, w in enumerate(combined_vocab):
        combined_vocab[i]=w.split(":", 1)[0]

# my custom code to create a super dictionary
combined_map = defaultdict(list)
with open("CombinedAllWords.txt") as f:
    for line in f:
        line = line.strip()
        splitted =  line.split(':')
        if len(splitted) > 1:
            word, meaning = splitted[0], splitted[1]
            combined_map[word].append(meaning)


#Open file and write sorted dictionary values into text file one by one in decreasing order
l = open("Words_Output.txt","w")

# for key, value in sorted(wordListToFreqDict(t).items(), key=lambda k,v: (v,k), reverse =True):
for key, value in sorted(wordListToFreqDict(combined_vocab).items(), key=lambda x: (x[1], x[0]), reverse =True):
    # l.write(" \n%s: %s" % (key, value))
    word = key
    freq = value
    meaning = combined_map[word]
    l.write("{}[{}]: {}\n".format(key, value, meaning))
l.close()
