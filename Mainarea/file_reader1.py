f = open("C:\PythonProjects\data_files\info1.txt", "r")
largest_number = 0
while True:
    the_value = f.readline()
    if len(the_value) > 0:
        number = int(the_value)
        if number > largest_number:
            largest_number = number
    else:
        break
#print(f.read())
#print (f.readline()) 
#print (f.read(6))
print (largest_number)



