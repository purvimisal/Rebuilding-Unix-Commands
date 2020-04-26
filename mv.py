# mv [Option] source destination
# mv stands for move. mv is used to move one or more files or directories from one place to another in file system like UNIX. 
# It has two distinct functions:
# -- It rename a file or folder.
# -- It moves group of files to different directory.


import os, sys
import shutil

args = sys.argv[1:]
source = args[0]
destination = args[1]

try: 
    if os.path.isdir(source):

        files = os.listdir(source)
        files.sort()
        for f in files:
            src = source+'/'+f
            dst = destination+'/'+f
            shutil.move(src,dst)
    else: 
        os.rename(source, destination)
except:
    print('Error in moving- check file or directory names')
