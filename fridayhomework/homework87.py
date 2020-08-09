list1 = []
ele = int(input("Type in the amount of elements"))
for i in range(0,ele):
    numbers = int(input("Enter the amount of numbers"))
    list1.append(numbers) 
squared = list(map(lambda a: a**2, list1))
cubed = list(map(lambda a: a**3, list1))
print (squared)
print (cubed)