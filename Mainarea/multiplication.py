def multiply(x,y):
    multiplication = x*y
    if multiplication <= 1000:
        return multiplication
    else:
        return x+y

number1 = int(input("Enter the first number "))
number2 = int(input("Enter the second number "))
product = multiply(number1, number2)
print ("The result is ", product)