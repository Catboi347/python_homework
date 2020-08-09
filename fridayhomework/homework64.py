numbers = [0,1,2,3,4,5,6]
for i in numbers:
    if i % 3 == 0:
        numbers.remove(i)
    if i == 0:
        numbers.insert(0,0)
print (numbers)