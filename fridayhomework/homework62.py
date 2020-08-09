f = open("C:\PythonProjects\data_files\guess_number.txt", "r")
number = f.readline()
right_number = int(number)
looped = False
while True:
    if looped == True:
        number_guess = int(input("Guess again ")) 
    else:
        number_guess = int(input("Guess a number between 0 and 9 "))
        looped = True
    if number_guess > 9:
        print ("Your number is too high")
    if number_guess < 0:
        print ("Your number is too low")
    if number_guess == right_number:
        print ("Well Guessed")
        break


