def sum(num):
    previousnumber = 0
    for i in range(num):
        sum1 = previousnumber + i
        print("Current Number =", i, "Previous Number = ", previousnumber," Sum = ", sum1)
        previousnumber = i
sum(10)