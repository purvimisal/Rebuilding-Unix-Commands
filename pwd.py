# pwd [OPTION]...
# pwd prints the name of the present/current working directory

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)