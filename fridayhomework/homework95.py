list1 = []
ele = int(input("Type in the amount of elements"))
for i in range(0,ele):
    numbers = int(input("Enter the amount of things you want in the list"))
    list1.append(numbers)
length_list = filter(lambda a: a if len(str(a))==6 else "", list1)
for l in length_list:
    print(i)


