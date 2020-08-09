import os
file_path = input("Type in a file path ")
print (os.access(file_path, os.W_OK))
print (os.path.dirname(file_path))
#print (os.path(file_path))