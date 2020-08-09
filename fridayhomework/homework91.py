from functools import reduce 
length = int(input("Type in the length of the method ")) 
fibonacci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fibonacci(length)) 
