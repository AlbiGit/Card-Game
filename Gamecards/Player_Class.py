from Card_Class import Card
from DeckOfCards_Class import DeckOfCards
import random
from random import randint
class Player:
    def __init__(self, name:str, number_of_cards_to_deal: int):
        if not 10 <= number_of_cards_to_deal <= 26:
            number_of_cards_to_deal = 26
        self.player_name = name
        self.player_hand = []
        self.cards_amount = number_of_cards_to_deal

    def set_hand(self, deck: DeckOfCards):
        for i in range(self.cards_amount):
            card = deck.deal_one()
            self.player_hand.append(card)

    def get_card(self):
        card = self.player_hand.pop(random.randint(0, len(self.player_hand) - 1))
        return card

    def add_card(self, card: Card):
        self.player_hand.append(card)
