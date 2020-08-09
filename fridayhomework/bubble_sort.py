list_random = [1,3,0,5,8,2,6]
while True:
    swapped = False
    for num in range(len(list_random)):
        if num < len(list_random)-1 and list_random[num] > list_random[num + 1]:
            num_current = list_random[num] 
            num_next = list_random[num + 1]
            list_random[num] = num_next
            list_random[num + 1] = num_current
            swapped = True
        print ("index =", num)  
        print (list_random)
    if swapped == False:
        break



