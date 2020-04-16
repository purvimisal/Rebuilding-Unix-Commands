#cp [OPTIONS] SOURCE... DESTINATION

#The SOURCE can contain one or more files or directories as arguments, and the DESTINATION argument can be a single file or directory .
#When the SOURCE and DESTINATION arguments are both files, the cp command copies the first file to the second one. 
# If the file doesn’t exists the command creates it.


import os
import shutil
import sys

args = sys.argv[1:]
sourcefile = args[0]
destination = args[1]

assert not os.path.isabs(sourcefile)


if not os.path.exists(destination):
    os.makedirs(destination)


if os.path.isdir(destination): 
    try:
        shutil.copy(sourcefile, destination)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())

else: 
    try:
        shutil.copyfile(sourcefile, destination)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        exit(1)


