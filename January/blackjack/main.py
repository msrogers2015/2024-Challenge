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
        self.values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        # Create a deck of cards
        self.create_deck()
        # Shuffle cards
        self.shuffle_deck()

    def create_deck(self, decks=1) -> None:
        '''Create a deck of cards'''
        # Create empty deck of cards
        self.deck = []
        # Create x amount of decks based on user input
        ### This feature will be added later.
        for deck in range(decks):
            # Loop through suits and values to create 52 cards
            for suit in self.suits.values():
                for value in self.values:
                    self.deck.append(f'{value}-{suit}')
    
    def shuffle_deck(self) -> None:
        '''Shuffle cards based on random seed using epoch time.'''
        # Shuffle deck 5-15 times
        for x in range(randint(5, 15)):
            shuffle(self.deck)

    def deal_card(self) -> str:
        '''Deal a single card if player chose hit.'''
        return self.deck.pop()

class Player:
    def __init__(self) -> None:
        '''Create instance of a player.'''
        # Create starting balance to bet with
        self.bank = 500
        # Create a list to hold current cards in hand.
        self.hand = []
        self.hand2 = []
        # Create a trigger to add cards to proper hand
        self.hand_toggle = False

    def get_value(self, hand) -> int:
        '''Add value of cards in players hand'''
        # Create a  value varible to total card values in player hand.
        hand_value = 0
        # Loop through player hand to get values or convert face cards and ace
        # cards to numerical value.
        for card in hand:
            # Get just the value of the card
            card_value = card.split('-')[0]
            # If card is numeric, add int to hand value
            if card_value.isdigit():
                hand_value += int(card_value)
            # If card is a face 
            elif card_value in ['J','Q','K']:
                hand_value += 10
            else:
                hand_value += 11
        # Check if player hand value is over 21 but the player hold aces.
        if (hand_value > 21 and 'A' in [card.split('-')[0] for card in hand]):
            # If player hold aces, remove 10 points per ace in hand while hand
            # value is above 21.
            for card in hand:
                if card.split('-')[0] == 'A' and hand_value > 21:
                    hand_value -= 10
        return hand_value

    def add_card(self, card) -> None:
        '''Add card to hand'''
        # If hand toggle is true, add card to second hand
        if self.hand_toggle:
            self.hand2.append(card)
        # Else, add card to main hand
        else:
            self.hand.append(card)

    def split_hand(self):
        '''Split hand into two hands.'''
        pass

    def print_hand(self, hand) -> None:
        '''Show player hand with suit icons'''
        # Create a local hand list to hold cards with the suit affixed to teh 
        local_hand = []
        # Loop through cards in hand
        for card in hand:
            # Add card to local hand list with the hyphen removed
            local_hand.append(''.join(card.split('-')))
        # Print hand with hyphens removed and end with a tab to display value
        print(','.join(local_hand), end='\t')
        # Display hand value
        print("Value: " + str(self.get_value(hand)))

class Dealer:
    def __init__(self) -> None:
        '''Create the dealer to play against.'''
        # Create list to hold current cards in hand
        self.hand = []

    def get_value(self) -> int:
        '''Get value of dealer hand'''
        # Create a local coount for hand value
        hand_value = 0
        # Loop through each hand in card
        for card in self.hand:
            # Split the suit from the value
            card_value = card.split('-')[0]
            # If number is digit, add value to local variable
            if card_value.isdigit():
                hand_value += int(card_value)
            # If value is face card, add 10
            elif card_value in ['J','Q','K']:
                hand_value += 10
            # Else, card is an ace so we add 11
            else:
                hand_value += 11
        # Check if hand is over 21 and if there are aces in dealers hand
        if (
            hand_value > 21 and
            'A' in [card.split('-')[0] for card in self.hand]):
            # Remove 10 from hand value for each ace while hand value is above
            # 21
            for card in self.hand:
                if card.split('-')[0] == 'A' and hand_value > 21:
                    hand_value -= 10
        # Return value of the hand
        return hand_value

    def print_hand(self) -> None:
        '''Show dealer hand with suit icons'''
        # Create a local hand list to hold cards with the suit affixed to teh 
        local_hand = []
        # Loop through cards in hand
        for card in self.hand:
            # Add card to local hand list with the hyphen removed
            local_hand.append(''.join(card.split('-')))
        # Print hand with hyphens removed and end with a tab to display value
        print(','.join(local_hand), end='\t')
        # Display hand value
        print("Value: " + str(self.get_value()))

class Game:
    def __init__(self) -> None:
        '''Initialize the game.'''
        # Create the player
        self.player = Player()
        # Create the dealer
        self.dealer = Dealer()
        # Create a bet counter.
        self.bet = 0
        # Create a blackjack flag
        self.blackjack1 = False
        self.blackjack2 = False
        # Create deck of cards
        self.deck = Deck()

    def start_game(self) -> None:
        '''Ask player to place a bet.'''
        # Set bet flag to None object
        bet = None
        # Loop as long as the player has not input valid data
        while bet is None:
            try:
                # Check if player has money in the bank.
                if self.player.bank > 0:
                    # Ask player for a bet as a whole number or quit the game
                    bet = (
                        input(f'Place your bet (max bet {self.player.bank}) '\
                              'or type "q" to quit: ')
                    )
                    # If player input is "q", exit the game
                    if bet.lower() == "q":
                        continue
                    # If player input is numeric, place bet
                    if bet.isdigit():
                        # Set game bet to twice the player bet and remove
                        # player bet from their bank.
                        self.bet = int(bet) * 2
                        self.player.bank -= int(bet)
                    # Raise value error is player input isn't q to quit or a 
                    # whole number
                    else:
                        # Reset bet variable to prevent code from exiting while
                        # loop
                        bet = None
                        raise ValueError
                # If player doesn'y have money in their bank, display game over
                # and exit game.
                else:
                    print('Your bank is empty, game over. :(')
                    break
            # If user does not enter a valid value, alert player of error and
            # try again.
            except ValueError:
                print('Please enter a whole number or "q" to quit the game.')
                # Give user time to read message.
                sleep(1)
                # Insert blank lines to seperate attempts
                print('\n')
        # If user didn't quit the game, continue to main gameplay.
        if bet.lower() != 'q':
            self.gameplay()
    
    def gameplay(self) -> None:
        '''Main gameplay loop for blackjack'''
        # Add two cards to player hand
        self.player.hand.append(self.deck.deal_card())
        self.player.hand.append(self.deck.deal_card())
        # While player can still make moves, loop actions
        while True:
            # Show player their current hand 
            self.player.print_hand(self.player.hand)
            # Set move flag to an empty string to prevent action loops
            move = ''
            # Set moves to an empty list
            moves = []
            # While the player has a valid hand (under 21), ask player to make
            # a move
            if self.player.get_value(self.player.hand) < 21:
                # If the player has two cards of the same value, allow player
                # to split hand into two hands and double the bet
                if (
                    len(self.player.hand) == 2 and
                    self.player.hand[0].split('-')[0] ==
                    self.player.hand[1].split('-')[0]):
                    moves = ['split','hit','stay']
                    move = input('Split, Hit or Stay? ')
                # Else, ask player if they want to draw another card or end
                # their turn.
                else:
                    moves = ['hit','stay']
                    move = input('Hit or Stay? ')
                # If player wants to draw a card, deal card
                if move.lower() == 'hit':
                    self.player.hand.append(self.deck.deal_card())
                # If player wants to end turn, break while loop
                elif move.lower() == 'stay':
                    break
                # If player wants to split hand, check if this move is valid.
                elif move.lower() == 'split' and move.lower() in moves:
                    print('Split hand')
                # If player types "q", quit the game.
                elif move.lower() == 'q':
                    break
                # If no valid moves are detected, alert player and retry.
                else:
                    print('Please enter a valid move.')
                    sleep(1)
            # IF player hand is over 21, end turn as a loss
            elif self.player.get_value(self.player.hand) > 21:
                print('You busted!')
                break
            # If player hand is 21, end turn as automatic win.
            elif self.player.get_value(self.player.hand) == 21:
                # Set blackjack flag to true.
                self.blackjack1 = True
                # Alert player of blackback and end gameplay cycle.
                print('Blackjack!')
                # Update player bank value
                self.player.bank += self.bet
                break
        # Check if player second hadn has a card
        if self.player.get_value(self.player.hand2) != 0:
            # If there is a card in the player second hand, add a second card
            # and start gameplay for second had
            self.player.hand2.append(self.deck.deal_card())
            while True:
                # Repeat the same base code as hand one with the second hand
                # minus the split option.
                if self.player.get_value(self.player.hand2) < 21:
                    move = input('Hit or Stay? ')
                    if move.lower() == 'hit':
                        self.player.hand2.append(self.deck.deal_card())
                    elif move.lower() == 'stay':
                        break
                    elif move.lower() == 'q':
                        break
                    else:
                        print('Please enter a valid move.')
                        sleep(1)
                    move = ''
                elif self.player.get_value(self.player.hand2) > 21:
                    print('You busted!')
                elif self.player.get_value(self.player.hand2) == 21:
                    self.blackjack2 = True
                    print("Blackjack!")
                    self.player.bank += self.bet
        # Start dealer play
        self.dealer_gameplay()
    
    def dealer_gameplay(self):
        '''Play the dealer hand.'''
        # Add two cards to dealer hand
        self.dealer.hand.append(self.deck.deal_card())
        self.dealer.hand.append(self.deck.deal_card())
        # While the dealer hand value is less than 17, add a card to.
        while self.dealer.get_value() < 17:
            self.dealer.hand.append(self.deck.deal_card())
            # Show dealer hand
            self.dealer.print_hand()
            # Wait one second to allow user to process dealer hand
            sleep(1)

if __name__ == '__main__':
    '''If the file is ran, start gameplay'''
    # Create an instance of the game class.
    game = Game()
    game.start_game()

