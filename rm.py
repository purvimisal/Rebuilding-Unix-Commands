#rm command is used to remove objects such as files, directories, symbolic links and so on from the file system like UNIX.


import sys
import os
import shutil

path = sys.argv[1]
 
if os.path.isdir(path):  
    try:
	    shutil.rmtree(path)
    except OSError as e:
	    print ("Error: %s - %s." % (e.filename,e.strerror))

elif os.path.isfile(path):  
    try:
        os.remove(path)
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.path,e.strerror))
else:
    print('Invalid Arguments')
    
