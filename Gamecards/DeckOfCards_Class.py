from Card_Class import Card
import random
class DeckOfCards:
    def __init__(self):
        """create a new deck and adds 52 cards to it"""
        self.deck = []
        for suit in [1, 2, 3, 4]:
            for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                self.deck.append(Card(value, suit))
        if len(self.deck) > 52:
            raise ValueError("Deck cant be larger than 52 cards")
        if type(suit) != int:
            raise TypeError("suit needs to be an int value")
        if type(value) != int:
            raise TypeError("Card value needs to be an int value")
        if value != range(1,13):
            raise ValueError("Card Value has to be between 1 - 13")
        if suit != range(1,4):
            raise ValueError("Card suit has to be betweeb 1 - 4")
        if self.deck is not []:
            raise TypeError("deck needs to be a dictionary type of array")

    def cards_shuffle(self):
        """shuffle the deck"""
        random.shuffle(self.deck)
        if self.deck == random.shuffle:
            random.shuffle(self.deck)

    def deal_one(self):
        """takes one card out of the deck and return it"""
        card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        if card !=
        return card
