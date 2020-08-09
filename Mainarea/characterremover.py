def removecharacters(str,n):
  return str[n:]
characters = input("Type a string in ")
number = int(input("Type in your number"))
if number < len(characters):
  print (removecharacters(characters, number))
else:
  print ("You're number should be less than the length of your string")
