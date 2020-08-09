import random

def count_carrots(list1, list2):
    carrot = 0
    for x in range(4):
        if list1[x] == list2[x]:
            carrot = carrot + 1
    return carrot

def count_sticks(list1, list2):
    sticks = 0
    for x in range(4):
        if list1[x] in list2 and list1[x] != list2[x]:
            sticks = sticks + 1
    return sticks 

random_list = []
for i in range (1000, 10000):
    random_list.append(i)
random_number = random.choice(random_list)
string_random_number = str(random_number)
number_guesses = 0
print ("You can only put in a 4 digit number")
print ("The number cannot have 0 in the front or back of the number")

while number_guesses < 10:
    string_guess_number = input("Input a number ")

    print (count_carrots(string_guess_number, string_random_number), "carrots")
    print (count_sticks(string_guess_number, string_random_number), "sticks")
    if string_guess_number == "0":
        print ("Did you read the instructions!")
        break
    if string_guess_number == string_random_number:
        print ("Well Played")
        break
    number_guesses = number_guesses + 1
    print ("----------------")
    #print ("You have used", number_guesses, "out of 10 turns")
    print ("You have", 10-number_guesses, "turns left")
    if 10 - number_guesses == 0:
        print ("You failed")
        print ("Better luck next time")
        


    
        


        



    
    