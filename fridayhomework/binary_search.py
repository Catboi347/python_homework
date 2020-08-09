import random
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
number = int(input("Input a number "))
list1 = []
for i in range(1, 101):
    list1.append(i)
    random_numbers = random.choices(list1, k=30)
    random_numbers.sort()
print (random_numbers)			
print(binary_search(random_numbers, number))