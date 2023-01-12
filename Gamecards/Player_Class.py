from Card_Class import Card
from DeckOfCards_Class import DeckOfCards
import random
class Player:
    def __init__(self, name:str, number_of_cards_to_deal: int):
        if not 10 <= number_of_cards_to_deal <= 26:
            number_of_cards_to_deal = 26
        self.player_name = name
        self.cards_amount = number_of_cards_to_deal

    def set_hand(self, deck: DeckOfCards):