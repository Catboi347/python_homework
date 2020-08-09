string1 = input("input a string ")
string2 = input("input another string ")
letter = input("input a letter ")
starts_with = lambda a: True if a.startswith(letter) else False
print (starts_with(string1))
starts_with = lambda a: True if a.startswith(letter) else False
print (starts_with(string2))
 