list1 = []
ele = int(input("Type in the amount of elements"))
for i in range(0,ele):
    numbers = int(input("Enter the amount of numbers"))
    list1.append(numbers)
odd_numbers = len(list(filter(lambda a:(a%2 != 0), list1)))
even_numbers = len(list(filter(lambda a:(a%2 == 0), list1)))
print (odd_numbers)
print (even_numbers)