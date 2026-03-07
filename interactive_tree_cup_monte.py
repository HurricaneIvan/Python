from random import shuffle
# def shuffle_cups(cups):
#     shuffle(cups)
#     return cups

def user_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1 or 2 \t")
    return int(guess)

def check_guess(cups, guess):
    win = cups.index("O")
    if (guess == win):
        print("You won!!!")
    else:
        print("Wrong Guess")
        print(cups)

def main():
    cups = ["O", " ", " "]
    shuffle(cups)
    guess = user_guess()
    check_guess(cups, guess)

if __name__ == "__main__":    main()
