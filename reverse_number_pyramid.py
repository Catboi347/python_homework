number = int(input("Type in a number between 1 and 9 "))
if number < 1  or number > 9:
    print ("Invalid number")
else:
    for i in range(0,number):
        for x in range(number-i,0,-1):
            print (x,end='')
        print()