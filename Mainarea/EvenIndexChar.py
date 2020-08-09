def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )
string = input("Please type in a string ")
print("The orginal string is ", string)
print("Printing only even index characters")
printEveIndexChar(string)