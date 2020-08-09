import random
list1 = []
list2 = []
for i in range(0, 10):
    list1.append(i) 
    list2.append(i)
a = random.choice(list1)
b = random.choice(list2)
print (a, b)
if a == b:
    print ("the numbers are equal")
else:
    print ("the numbers are NOT equal")