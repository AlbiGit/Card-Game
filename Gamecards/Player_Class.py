from Card_Class import Card
from DeckOfCards_Class import DeckOfCards
import random
class Player:
    def __init__(self, name:str, number_of_cards_to_deal: int):
        """sets a new player"""
        if not 10 <= number_of_cards_to_deal <= 26:
            number_of_cards_to_deal = 26
        self.player_name = name
        self.player_hand = []
        self.cards_amount = number_of_cards_to_deal

    def set_hand(self, deck: DeckOfCards):
        """sets the player's hand according to the amount of cards entered at the beginning of the game"""
        for i in range(self.cards_amount):
            card = deck.deal_one()
            self.player_hand.append(card)

    def get_card(self):
        """takes one card out of the player's hand and returns it"""
        card = self.player_hand.pop(random.randint(0, len(self.player_hand) - 1))
        return card

    def add_card(self, card: Card):
        """adds a card to the player's hand"""
        self.player_hand.append(card)
