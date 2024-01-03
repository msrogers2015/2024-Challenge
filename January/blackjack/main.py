from random import shuffle, randint

class Deck:
    def __init__(self) -> None:
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

    def create_deck(self) -> None:
        '''Create a deck of cards'''
        # Create empty deck of cards
        self.deck = []
        # Loop through suits and values to create 52 cards
        for suit in self.suits:
            for value in self.values:
                self.deck.append(f'{value}-{suit}')
    
    def shuffle_deck(self) -> None:
        '''Shuffle cards based on random seed using epoch time.'''
        # Shuffle deck 3-10 times
        for x in range(randint(3, 10)):
            shuffle(self.deck)

    def deal_hand(self) -> list:
        '''Deal initial cards to start round.'''
        pass

    def deal_card(self) -> str:
        '''Deal a single card if player chose hit.'''
        pass

class Player:
    def __init__(self) -> None:
        '''Create instance of a player.'''
        # Create starting balance to bet with
        self.bank = 500
        # Create a list to hold current cards in hand.
        self.hand = []
        self.hand2 = []

    def get_value(self, hand) -> int:
        '''Add value of cards in players hand'''
        # Create a  value varible to total card values in player hand.
        hand_value = 0
        # Loop through player hand to get values or convert face cards and ace
        # cards to numerical value.
        for card in hand:
            card_value = card.split('-')[0]
            if card_value.isdigit():
                hand_value += int(card_value)
            elif card_value in ['J','Q','K']:
                hand_value += 10
            else:
                hand_value += 11
        # Check if player hand value is over 21 but the player hold aces.
        if (hand_value > 21 and
            'A' in [card.split('-')[0] for card in hand]):
            # If player hold aces, remove 10 points per ace in hand while hand
            # value is above 21.
            for card in hand:
                if card.split('-')[0] == 'A' and hand_value > 21:
                    hand_value -= 10
        return hand_value

    def add_card(self):
        '''Add card to hand'''
        pass

    def split_hand(self):
        '''Split hand into two hands.'''
        pass

if __name__ == '__main__':
    # Test code via running it from the main file. Actual game loop
    # will be placed in a Gameplay class.
    player = Player()
    player.hand = ['A-D', '4-H', '3-H', 'A-S']
    player.get_value()