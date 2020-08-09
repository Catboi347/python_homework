numbers = []
for i in range(100, 401):
    string = str(i)
    if (int(string)) % 2 == 0:
        numbers.append(string)
print (",".join(numbers))