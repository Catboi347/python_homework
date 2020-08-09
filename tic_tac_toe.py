import random

spot_available = True


the_board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
            
def print_board(board):
    print (board["7"] + "|" + board["8"] + "|" + board["9"])
    print ("-+-+-")
    print (board["4"] + "|" + board["5"] + "|" + board["6"])
    print ("-+-+-")
    print (board["1"] + "|" + board["2"] + "|" + board["3"])

def random_O():
    list1 = []
    for i in range(1, 10):
        if the_board[str(i)] == " ":
            list1.append(str(i))
    if len(list1) == 0:
        spot_available = False
        return 

    random_number = random.choice(list1)
    if the_board[random_number] == " ":
        the_board[random_number] = "O"

def game():

    turn = "X"
    count = 0
    
    for i in range(10):
        if spot_available == False:   
            return "End of game"

        print_board(the_board)
        move = input("It's your turn," + turn + ". Move to which place? ")

        if the_board[move] == " ":
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")
            continue

        print (random_O())

        if the_board["7"] == the_board["8"] == the_board["9"] != " ":
            print_board(the_board)
            print("Game Over.")             
            print(turn + " won!")                
            break
        elif the_board["4"] == the_board["5"] == the_board["6"] != ' ':
            print_board(the_board)
            print("Game Over.")                
            print(turn + " won!")  
            break
        elif the_board["1"] == the_board["2"] == the_board["3"] != ' ': 
            print_board(the_board)
            print("Game Over.")              
            print(turn + " won!")  
            break
        elif the_board["1"] == the_board["4"] == the_board["7"] != ' ': 
            print_board(the_board)
            print("Game Over.")               
            print(turn + " won!")  
            break
        elif the_board["2"] == the_board["5"] == the_board["8"] != ' ': 
            print_board(the_board)
            print("Game Over.")                
            print(turn + " won!")  
            break
        elif the_board["3"] == the_board["6"] == the_board["9"] != ' ': 
            print_board(the_board)
            print("Game Over.")                
            print(turn + " won!")  
            break 
        elif the_board["3"] == the_board["5"] == the_board["7"] != ' ': 
            print(print_board(the_board))
            print("Game Over.")              
            print(turn + " won!")  
            break
        elif the_board["1"] == the_board["5"] == the_board["9"] != ' ': 
            print(print_board(the_board))
            print("Game Over.")                
            print(turn + " won!")  
            break 

        if count == 8:
            print("Game Over.")                
            print("It's a Tie!!")

print (game())               