list_random = [1,3,0,5,8,2,6]
print ("Original List: ")
print (list_random)
print ("Process: ")
for i in range(len(list_random)):
    print (list_random) 
    smallest_number = i 
    for j in range(i+1, len(list_random)): 
        if list_random[smallest_number] > list_random[j]: 
            smallest_number = j         
    list_random[i], list_random[smallest_number] = list_random[smallest_number], list_random[i] 
print ("Sorted List: ")
print (list_random)