import os
import sys
import time
import stat
path = input("type in a directory name")
print('Path Name :', path)
print('Size:', stat(path).ST_SIZE)
print('Permissions:', stat(path).ST_MODE)
print('Owner:', path).ST_UID)
print('Device:', path.ST_DEV)
print('Created     :', path.time.ctime(stat.ST_MTIME))
print('Last modified:', path.time.ctimestat.ST_CTIME)
print('Last accessed:', path.stat.ST_ATIME)