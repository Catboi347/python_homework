def mergelist(list_one, list_two):
    print("The first list is: ", list_one)
    print("The second list is: ", list_two)
    third_list = []    
    for num in list_one:
        if num % 2 != 0:
            third_list.append(num)
    for num in list_two:
        if num % 2 == 0:
            third_list.append(num)
    return third_list
list_one = [10, 20, 23, 11, 17]
list_two = [13, 43, 24, 36, 12]
print("The result list is:", mergelist(list_one, list_two))