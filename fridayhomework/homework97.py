list1 = []
ele = int(input("Type in the amount of elements"))
for i in range(0,ele):
    numbers = int(input("Enter the amount of numbers"))
    list1.append(numbers)
divider = list(filter(lambda a: a % 19 == 0 or a % 13 == 0, list1))
print (divider)