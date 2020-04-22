# md5sum [OPTION]... [FILE]...
# The md5sum is designed to verify data integrity using MD5 (Message Digest 5).
# MD5 is 128-bit cryptographic hash and if used properly it can be used to verify file authenticity and integrity.

from hashlib import md5
import sys

m = md5()
buf_size = 8192
try:
    filename = sys.argv[1]
    with open(filename, 'rb') as f:
        data = f.read(buf_size)
        while data:
            m.update(data)
            data = f.read(buf_size)
    print(m.hexdigest(),' ', filename)
except: 
    print('Please provide a file as argument in format: python3 md5sum.py [FILE]...')