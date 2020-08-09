def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest
number1 = int(input("Type in a number"))
number2= int(input("Type in another number"))
number3 = int(input("Type in a third number"))
print (maximum(number1, number2, number3))