# head [OPTION]... [FILE]...
# The head command, as the name implies, print the top N number of data of the given input. 
# By default, it prints the first 10 lines of the specified files. 

import sys

args = sys.argv[1:]
numberOfLines = 10 #DEFAULT 
fileName = ''
for i in args: 
    if i.startswith('-'):
        i = i.strip('-')
        numberOfLines = int(i)
    else:
        fileName = i
 
fileHandler = open(fileName, 'r' )

lines = []

while len(lines) < numberOfLines:
    lines.append(fileHandler.readline())
fileHandler.close()

#printing lines
for line in lines:
    print(line, end="")