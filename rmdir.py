# rmdir [OPTION]... DIRECTORY...
# Remove the DIRECTORY(ies), if they are empty. 

import sys
import os
import shutil

path = sys.argv[1]
 
if os.path.isdir(path):  
    if len(os.listdir(path) ) == 0:
        try:
	        shutil.rmtree(path)
        except OSError as e:
	        print ("Error: %s - %s." % (e.filename,e.strerror))
    else:    
        print("Directory is not empty")
else: 
    print("Directory does not exist")
