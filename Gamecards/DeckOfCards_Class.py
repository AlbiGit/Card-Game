from Card_Class import Card
import random
class DeckOfCards:
    def __init__(self):
        """create a new deck and adds 52 cards to it"""
        self.deck = []
        for suit in [1, 2, 3, 4]:
            for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                self.deck.append(Card(value, suit))
        if len(self.deck) != 52:
            raise ValueError("Deck must be 52 cards")
        if type(self.deck) != list:
            raise TypeError("deck needs to be a list type of array")

    def cards_shuffle(self):
        """shuffle the deck"""
        if self.deck == []:
            raise ValueError("can't shuffle an empty deck")
        # makes a copy of the deck
        copy_deck = self.deck.copy()
        random.shuffle(self.deck)
        # after the shuffle, checks that the new order is different from before the shuffle
        while self.deck == copy_deck:
            random.shuffle(self.deck)

    def deal_one(self):
        """takes one card out of the deck and return it"""
        if len(self.deck) == 0:
            print(f"deck has no more cards left")
            return None
        elif len(self.deck) == 1:
            card = self.deck.pop(0)
            return card
        else:
            card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        return card