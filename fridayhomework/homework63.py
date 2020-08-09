numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_number = 0
odd_number = 0
for i in numbers:
    if i % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
print ("Amount of even numbers =", even_number)
print ("Amount of odd numebrs =", odd_number)
