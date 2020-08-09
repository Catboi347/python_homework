import random
random_list = ["rock", "paper", "scissors"]
game_turns = 0
bot = 0
player = 0
game_length = 3
print ("This is rock paper scissors")

while game_turns < game_length:
    rock_paper_scissors_choice = input("Choose rock papers or scissors ")
    game_turns = game_turns+1
    random_choice = random.choice(random_list)
    if (random_choice == "paper" and rock_paper_scissors_choice == "rock") or (random_choice == "rock" and rock_paper_scissors_choice == "scissors") or (random_choice == "scissors" and rock_paper_scissors_choice == "paper"):
        bot = bot+1
    elif (random_choice == "rock" and rock_paper_scissors_choice == "paper") or (random_choice == "scissors" and rock_paper_scissors_choice == "rock") or (random_choice == "paper" and rock_paper_scissors_choice == "scissors"):
        player = player+1
    if rock_paper_scissors_choice == random_choice:
        print ("tie")
        game_length = game_length+1
    print ("Bot chose ", random_choice)
    print ("player:", player)
    print ("bot:", bot)
#break main and rock paper scissors into functions
#
