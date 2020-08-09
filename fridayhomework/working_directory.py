import os
print (os.getcwd())
os.chdir("..")
print (os.path.abspath(os.curdir))