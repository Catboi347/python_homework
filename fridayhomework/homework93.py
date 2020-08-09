list1 = []
ele = int(input("Type in the amount of elements"))
for i in range(0,ele):
    numbers = int(input("Enter the amount of things you want in the list"))
    list1.append(numbers)
rearrange_lists = [x for x in list1 if x<0] + [x for x in list1 if x>=0]
print (rearrange_lists)