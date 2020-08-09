sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
tuple_creator = tuple(sampleList)
updated_list = []
for x in sampleList:
    count = updated_list.count(x)
    if count == 0:
        updated_list.append(x)
tuple_creator = tuple(updated_list)
print (updated_list)
print (tuple_creator)    
updated_list.sort()
print (updated_list[0])
updated_list.sort(reverse=True)
print (updated_list[0])
     