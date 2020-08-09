import re
string = input("Type in a string ")
string_determiner = lambda x: True if ((re.search("[a-z]", x)) or (re.search("[A-Z]", x))) else False
result = string_determiner(string)
print (result)