from random import shuffle, randint
import time

class Deck:
    def __init__(self):
        '''Create information to build a deck of cards.'''
        # Create suit denominations
        self.suits = {
            "D": u"\u2666",  # diamonds
            "H": u"\u2665",  # hearts
            "C": u"\u2663",  # clubs
            "S": u"\u2660"  # spades
        }
        # Create values
        self.values = ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']

    def create_deck(self):
        '''Create a deck of cards'''
        # Create empty deck of cards
        self.deck = []
        # Loop through suits and values to create 52 cards
        for suit in self.suits:
            for value in self.values:
                self.deck.append(f'{value}-{suit}')
    
    def shuffle_deck(self):
        '''Shuffle cards based on random seed using epoch time.'''
        # Shuffle deck 3-10 times
        for x in range(randint(3, 10)):
            shuffle(self.deck)

    def deal_hand(self):
        '''Deal initial cards to start round.'''
        pass

if __name__ == '__main__':
    # Test code via running it from the main file. Actual game loop
    # will be placed in a Gameplay class.
    deck = Deck()
    deck.create_deck()
    deck.shuffle_deck()
    print(deck.deck)
    for card in deck.deck:
        value, suit = card.split('-')
        print(f'{value}{deck.suits[suit]}')