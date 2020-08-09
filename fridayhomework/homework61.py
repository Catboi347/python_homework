c = int(input("Input your celcius "))
f = int(input("Input your faranheit "))
c_to_f = (c/5)*9 + 32
f_to_c = ((f-32)*5)/9
print (str(c) + "°C", "is equal to", str("{:.1f}".format(c_to_f)) + "°F")
print (str(f) + "°F", "is equal to", str("{:.1f}".format(f_to_c)) + "°C")
#print ("{:.2f}".format(A), "units squared")