list1 = []
ele1 = int(input("Type in the amount of elements"))
for i in range(0,ele1):
    numbers1 = int(input("Enter the amount of things you want in the list"))
    list1.append(numbers1)
list2 = []
ele2 = int(input("Type in the amount of elements"))
for i in range(0,ele2):
    numbers2 = int(input("Enter the amount of things you want in the list"))
    list2.append(numbers2)
combined_list = list(map(lambda x, y: x + y, list1, list2))
print (combined_list)