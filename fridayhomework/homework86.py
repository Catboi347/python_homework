list1 = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20]
even_numbers = list(filter(lambda x: x%2 == 0, list1))
odd_numbers = list(filter(lambda x: x%2 != 0, list1))
print (even_numbers)
print (odd_numbers)
