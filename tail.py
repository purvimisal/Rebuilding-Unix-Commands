# tail [OPTION]... [FILE]...
# The tail commands is the complementary of head command and prints the last N number of data of the given input. 
# By default it prints the last 10 lines of the specified files. 

import os
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

lines = []

with open(fileName, 'rb') as read_obj:
    read_obj.seek(0, os.SEEK_END)
    buf = bytearray()
    pointer = read_obj.tell()
    while pointer >= 0:
        read_obj.seek(pointer)
        pointer = pointer -1
        new_byte = read_obj.read(1)
        if new_byte == b'\n':
            lines.append(buf.decode()[::-1])
            if len(lines) == numberOfLines:
                pointer = -1
            buf= bytearray()
        else:
            buf.extend(new_byte)

    if len(buf) > 0:
        lines.append(buf.decode()[::-1])
 
#printing lines
for line in list(reversed(lines)):
    print(line, end="\n")