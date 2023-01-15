from Card_Class import Card
from Player_Class import Player
from DeckOfCards_Class import DeckOfCards

class CardGame:
    def __init__(self, name1: str, name2: str, cards_to_each_player: int):
        """creates a new game with 2 players"""
        if type(cards_to_each_player) != int:
            raise TypeError("Number of cards needs to be an int value")
        if not 10 <= cards_to_each_player <= 26:
            cards_to_each_player = 26
            print("game gets set to 26 cards each!")
        if type(name1) != str:
            raise TypeError("Player name needs to be a string value")
        if type(name2) != str:
            raise TypeError("Player name needs to be a string value")
        self.player_a = Player(name1, cards_to_each_player)
        self.player_b = Player(name2, cards_to_each_player)
        self.game_deck = DeckOfCards()
        self.new_game()
    def new_game(self):
        """shuffle the deck and deal cards to the players"""
        self.game_deck.cards_shuffle()
        self.player_a.set_hand(self.game_deck)
        self.player_b.set_hand(self.game_deck)

    def get_winner(self):
        if len(self.player_a.player_hand) == len(self.player_b.player_hand):
            return None
        else:
            if len(self.player_a.player_hand) > len(self.player_b.player_hand):
                return self.player_a
            else:
                return self.player_b
