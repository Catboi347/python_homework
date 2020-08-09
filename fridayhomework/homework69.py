string = input("Type in a string ")
digit = 0
letter = 0
for x in string:
    if x.isdigit():
        digit += 1
    else:
        letter += 1
print ("letters", letter)
print ("digits", digit)

