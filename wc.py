# wc - print newline, word, and byte counts for each file
# wc's general syntax:
# wc [OPTION]... [FILE]...
# wc [OPTION]... --files0-from=F



import operator

import sys

args = sys.argv[1:]
options = []
files = []
for i in args: 
    if i.startswith('-'):
        i = i.strip('-')
        options.extend([x for x in i])
    else:
        files.append(i)




def create_dictionary(wordlist):
    word_count = {}
    sorted_list = []
    for word in wordlist:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        sorted_list.append([key, value])
    print(sorted_list)
    return word_count

wordList = []
filename = files[0]
with open(filename, 'r') as file:
    for line in file:
        words = line.lower().split() 
        for each_word in words:
            #print(each_word)
            wordList.append(each_word)
  
print(sum(create_dictionary(wordList).values()))