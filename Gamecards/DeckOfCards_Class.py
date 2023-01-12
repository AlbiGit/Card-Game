from Card_Class import Card
import random
class DeckOfCards:
    def __init__(self):
        """create a new deck and adds 52 cards to it"""
        self.deck = []
        for suit in [1, 2, 3, 4]:
            for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                self.deck.append(Card(value, suit))

    def cards_shuffle(self):
        """shuffle the deck"""
        random.shuffle(self.deck)

    def deal_one(self):
        """takes one card out of the deck and return it"""
        card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        return card
