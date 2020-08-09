import re
string = input("Type in a string ")
if re.search("[a-z]", string):
    print ("This is a string ")
elif re.search("[A-Z]", string):
    print ("This is a string")
else:
    print ("This is an integer")