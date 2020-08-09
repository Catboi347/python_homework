def sum(number):
    if number:
        return number + sum(number-1)
    else:
        return 0
the_number = int(input("Type in your number "))
sum1 = sum(the_number)
print(sum1)