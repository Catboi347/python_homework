joiner = []
binary = [x for x in input().split(",")]
print (binary)
for y in binary:
    divisible = int(y)
    if divisible % 5 == 0:
        joiner.append(y)
print (",".join(joiner))