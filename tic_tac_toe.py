import random

def board_game(board):
    for i in board:
        print(i)

def user_guess(board):
    loop = True
    while loop:
        row, col = map(int, input("Enter numbers (0-2) separated by a space for row and column: ").split())
        if board[row][col] == " ":
            loop = False
            board[row][col] = "X"

def bot_guess(board):
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
    if all(item == "X" for item in major):
        print("You won!!!")
        result = False
    if all(item == "O" for item in board[i]):
        print("You Lose")
        result = False

    return result

def check_status(board):
    if check_columns(board) and check_rows(board) and check_diagonal(board):
        return True
    else:
        return False

def main():
    new_board = [[" ", " ", " "], 
             [" ", " ", " "], 
             [" ", " ", " "]]
    board = new_board.copy()
    loop = True
    while loop:
        board_game(board)
        user_guess(board)
        bot_guess(board) 
        loop = check_status(board)
        print("Thanks for playing")
        
if __name__ == "__main__":    main()