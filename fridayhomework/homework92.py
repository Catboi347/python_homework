list1 = []
ele = int(input("Type in the amount of elements"))
for i in range(0,ele):
    numbers = input("Enter the amount of things you want in the list")
    list1.append(numbers)
list2 = []
ele2 = int(input("Type in the amount of elements"))
for i in range(0,ele):
    numbers2 = input("Enter the amount of things you want in the list")
    list2.append(numbers2)
intersection = list(filter(lambda x: x in list1, list2))
print (intersection)