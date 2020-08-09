def reversecheck(number):
    print("original number", number)
    originalnumber = number
    size = int(len(originalnumber))
    reversenumber = ""
    print (str(size))
    for x in range(size):
        print ("x=" + str(x))
        print (originalnumber[size-x-1:size-x])
        reversenumber = reversenumber + originalnumber[size-x-1:size-x]
        print (reversenumber)
    return reversenumber

numbers = input("Type in a number")
altnumbers = reversecheck(numbers)
print ("reverse number;" + altnumbers)
if numbers == altnumbers:
    print ("True")
else:
    print ("False")
#print("The original and reverse number is the same:", reversecheck(numbers))