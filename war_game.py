import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    

class Deck():
    
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) ==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'


def main():
    player1 = Player("One")
    player2 = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        player1.add_cards(new_deck.deal_one())
        player2.add_cards(new_deck.deal_one())

    game_status = True
    round_num = 0
    
    while game_status:
        round_num += 1
        print(f'Round {round_num}')
        
        if len(player1.all_cards) == 0:
            print('Player One is out of cards, Player Two wins!!!')
            game_status == False
            break
        
        if len(player2.all_cards) == 0:
            print('Player Two is out of cards, Player One wins!!!')
            game_status == False
            break
        
        # Start a New Round
        player1_cards = []
        player1_cards.append(player1.remove_one())
        player2_cards = []
        player2_cards.append(player2.remove_one())

        # At War
        war = True
        while war:

            if player1_cards[-1].value > player2_cards[-1].value:
                player1.add_cards(player1_cards)
                player1.add_cards(player2_cards)
                war = False
            elif player1_cards[-1].value < player2_cards[-1].value:
                player2.add_cards(player1_cards)
                player2.add_cards(player2_cards)
                war = False
            else:
                print("War!")
                if len(player1.all_cards) < 5:
                    print("Player one unable to declare war")
                    print("Player two wins")
                    game_status = False
                    break
                elif len(player2.all_cards) < 5:
                    print("Player two unable to declare war")
                    print("Player one wins")
                    game_status = False
                    break
                else:
                    for num in range(5):
                        player1_cards.append(player1.remove_one())
                        player2_cards.append(player2.remove_one())

if __name__ == "__main__":    main()