from Card_Class import Card
import random
from random import randint

class DeckOfCards:
    def __init__(self):
        self.deck = []
        for suit in [1, 2, 3, 4]:
            for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                self.deck.append(Card(value, suit))

    def cards_shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        self.deck.pop(random.randint(0, len(self.deck) - 1))