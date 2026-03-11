import copy
import random


def display_board(board):

    for i in board:
        print(i)

def shuffle_start():
    return random.choices([0, 1], k =1)

def player1_guess(board):
    loop = True
    while loop:
        row = ''
        col = ''
        while row not in [0,1,2] and col not in [0, 1, 2]:
            row, col = map(int, input("Enter numbers (0-2) separated by a space for row and column: ").split())
            if row not in [0,1,2]:
                print("Invalid input, Please Try Again")
            elif board[row][col] == " ":
                loop = False
                board[row][col] = "X"

def player2_guess(board):
    options = [0, 1, 2]
    loop = True
    while loop:
        row, col = random.choices(options, k=2)
        if board[row][col] == " ":
            loop = False
            board[row][col] = "O"

def check_columns(board):
    result = True
    columns = list(zip(*board))
    for elm in columns:
        if all(item == "X" for item in elm):
            print("You won!!!")
            result = False
        if all(item == "O" for item in elm):
            print("You Lose")
            result = False
    return result

def check_rows(board):
    result = True
    for i in range(0, 3):
        
        if all(item == "X" for item in board[i]):
            print("You won!!!")
            result = False
        elif all(item == "O" for item in board[i]):
            print("You Lose")
            result = False
    return result

def check_diagonal(board):
    result = True
    major = []
    minor = []
    for i in range(0, 3):
        major.append(board[i][i])
        minor.append(board[i][2-i])
    if all(item == "X" for item in major) :
        print("You won!!!")
        result = False
    elif all(item == "X" for item in minor) :
        print("You won!!!")
        result = False
    elif all(item == "O" for item in major):
        print("You Lose")
        result = False
    elif all(item == "O" for item in minor):
        print("You Lose")
        result = False

    return result

def check_tie(board):
    count = 0
    for elm in board:
        if all(item != " " for item in elm):
            count += 1
    
    if count == 3:
        print("Players tied")
        return False

def check_status(board):
    if check_columns(board) and check_rows(board) and check_diagonal(board):
        return True
    else:
        return False

def main():

    new_board = [[" "," "," "],
                 [" "," "," "], 
                 [" "," "," "]] 
 
    board = ''
    spaces = 9
    new_game = True
    current_game = True
    starter = shuffle_start()[0]
    if starter == 0:
        # player1 start scenario
        while current_game:
            if new_game:
                board = copy.deepcopy(new_board)
                new_game = False
        
            display_board(board)
            if spaces > 1:
                player1_guess(board)
                player2_guess(board)
                spaces -= 2
                if check_status(board) == False:
                    display_board(board)
                    ans = input("Do you want to play again? Y or N ")
                    if ans == "Y":
                        new_game = True
                        current_game = True
                    else:
                        print("Thanks for playing")
                
            elif spaces == 1:
                player1_guess(board)
                spaces -= 1
                current_game = False
                if check_tie(board) == False:
                    ans = input("Do you want to play again? Y or N ")
                    if ans == "Y":
                        new_game = True
                        current_game = True
                        spaces = 9
                    else:
                        print("Thanks for playing")

    else:
        # player2 start scenario
        print("Bot plays first")
        while current_game:
            if new_game:
                print("here")
                board = copy.deepcopy(new_board)
                player2_guess(board)
                spaces -= 1
                new_game = False

            display_board(board)
            if spaces > 1:
                player1_guess(board)
                player2_guess(board)
                spaces -= 2
                if check_status(board) == False:
                    display_board(board)
                    ans = input("Do you want to play again? Y or N ")
                    if ans == "Y":
                        new_game = True
                        current_game = True
                    else:
                        print("Thanks for playing")
                print(f'spaces {spaces}')
            elif spaces == 0:
                current_game = False
                if check_tie(board) == False:
                    ans = input("Do you want to play again? Y or N ")
                    if ans == "Y":
                        new_game = True
                        current_game = True
                        spaces = 9
                    else:
                        print("Thanks for playing")
        

if __name__ == "__main__":    main()