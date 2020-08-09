import os
def getlistoffiles(folder_name):
    folder_items = os.listdir(folder_name)
    for f in folder_items:
        fullPath = os.path.join(folder_name, f)
        if os.path.isdir(fullPath):
            print ("directory:", fullPath)
            getlistoffiles(fullPath)
        else:
            print ("file:", fullPath)

getlistoffiles("C:\PythonProjects")

