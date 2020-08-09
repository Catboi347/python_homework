list1 = []
ele = int(input("Type in the amount of elements"))
for i in range(0,ele):
    numbers = int(input("Enter the amount of things you want in the list"))
    list1.append(numbers)
even_numbers = len(list(filter(lambda a: a%2 == 0, list1)))
odd_numbers = len(list(filter(lambda a: a%2 != 0, list1)))
print (even_numbers, odd_numbers)
