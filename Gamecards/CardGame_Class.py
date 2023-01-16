from Player_Class import Player
from DeckOfCards_Class import DeckOfCards
class CardGame:
    # Setup for the card game with 2 player names
    # and how many cards each player will hold at the start
    def __init__(self, name1, name2, cards_to_each_player):
        if type(cards_to_each_player) != int:
            raise TypeError("Number of cards needs to be an int value")
        if not 10 <= cards_to_each_player <= 26:
            cards_to_each_player = 26
            print("game gets set to 26 cards each!")
        if type(name1) != str:
            raise TypeError("Player name needs to be a string value")
        if name1 == '':
            raise ValueError("the name can't be empty")
        if type(name2) != str:
            raise TypeError("Player name needs to be a string value")
        if name2 == '':
            raise ValueError("the name can't be empty")
        self.player_a = Player(name1, cards_to_each_player)
        self.player_b = Player(name2, cards_to_each_player)
        self.game_deck = DeckOfCards()
        self.new_game()

    # New game function where it starts of by shuffling the deck and sets both players hands
    # each player starts of with the number of cards that's set at the start of the game
    def new_game(self):
        self.game_deck.cards_shuffle()
        self.player_a.set_hand(self.game_deck)
        self.player_b.set_hand(self.game_deck)

    # Get winner function that calculates the games winner by the number of cards in a players hand
    # the function should be called upon at the end of the game but can be called upon at any time
    def get_winner(self):
        if len(self.player_a.player_hand) == len(self.player_b.player_hand):
            return None
        else:
            if len(self.player_a.player_hand) > len(self.player_b.player_hand):
                return self.player_a
            else:
                return self.player_b
