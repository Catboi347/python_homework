fibonacci = [0, 1]
for num in range(8):
    num = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(num)
print(fibonacci)
