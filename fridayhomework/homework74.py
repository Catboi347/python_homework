dogs_age = int(input("input the age of your dog in human years "))
if dogs_age <= 0:
    print ("The age has to be a positive number ")
elif dogs_age <= 2:
    dog_years = dogs_age*10.5
else:
    dog_years = 21 + (dogs_age - 2)*4
print ("The dog's age in dog's years is", dog_years) 