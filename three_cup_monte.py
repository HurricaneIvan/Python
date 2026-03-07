from random import shuffle

def shuffle_cups(cups):
    shuffle(cups)
    return cups

def find_ball(cups):
    return cups.index('ball')

def main():
    cups = ['ball', 'empty', 'empty']
    shuffle_cups(cups)
    position = find_ball(cups)
    print(f"The ball is under cup number {position + 1}.")
if __name__ == "__main__":    main()

