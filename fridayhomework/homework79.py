print ("Input lengths of the triangle sides:")
x = input("x:")                                                                    
y = input("y:")                                                                    
z = input("z:")
if (x == y) and (x == z) and (y == z):
    print ("equilateral triangle")
elif (x == y) or (x == z) or (y == z):
    print ("isosceles triangle")
else:
    print ("Scalene triangle")
                                    