def flatten(list_of_lists):
    flat_list = []
    for elem in list_of_lists: 
        for item in elem:
            flat_list.append(item)
    
    return flat_list

print (flatten([[1, 2], [3, 4]]))