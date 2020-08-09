def largest_difference(num_list):
    min_list = min(num_list)
    max_list = max(num_list)
    return (max_list-min_list)
    
print (largest_difference([1, 2, 3]))