from random import shuffle, randint
from time import sleep

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
        self.split_flag = False

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

    def add_card(self, card) -> None:
        '''Add card to hand'''
        if self.split_flag is False:
            self.hand.append(card)

    def split_hand(self):
        '''Split hand into two hands.'''
        pass

    def print_hand(self) -> None:
        pass

class Dealer:
    def __init__(self) -> None:
        '''Create the dealer to play against.'''
        # Create list to hold current cards in hand
        self.hand = []

    def set_hand(self) -> None:
        pass

    def print_hand(self) -> None:
        pass

class Game:
    def __init__(self) -> None:
        '''Initialize the game.'''
        # Create the player
        self.player = Player()
        # Create the dealer
        self.dealer = Dealer()
        # Create a bet counter.
        self.bet = 0

    def start_game(self) -> None:
        '''Ask player to place a bet.'''
        # Set bet flag to None object
        bet = None
        # Loop as long as the player has not input valid data
        while bet is None:
            try:
                if self.player.bank > 0:
                    # Ask player for a bet as a whole number or quit the game
                    bet = (
                        input(f'Place your bet (max bet {self.player.bank}) '\
                              'or type "q" to quit: ')
                    )
                    # If player input is "q", exit the game
                    if bet.lower() == "q":
                        break
                    # If player input is numeric, place bet
                    if bet.isdigit():
                        # Set game bet to twice the player bet and remove
                        # player bet from their bank.
                        self.bet = int(bet) * 2
                        self.player.bank -= int(bet)
                    # Raise value error is player input isn't q to quit or a 
                    # whole number
                    else:
                        bet = None
                        raise ValueError
                else:
                    print('Your bank is empty, game over. :(')
                    break
            # If user does not enter a valid value, alert player of error and
            # try again.
            except ValueError:
                print('Please enter a whole number or "q" to quit the game.')
                # Give user time to read message.
                sleep(1)
                print('\n'*2)

if __name__ == '__main__':
    '''If the file is ran, start gameplay'''
    # Create an instance of the game class.
    game = Game()
    game.start_game()

