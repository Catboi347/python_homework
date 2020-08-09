def only_ints(number1, number2):
    check_number = 0
    if type(number1) == type(check_number) and type(number2) == type(check_number):
        number_check = True 
    else:
        number_check = False
    return number_check

print (only_ints("a", 3))
print (only_ints(2, 3))