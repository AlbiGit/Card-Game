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
        if not 1 <= value <= 13:
            raise ValueError('card value must be between 1 to 13')
        if not 1 <= suit <= 4:
            raise ValueError('card symbol must be between 1 to 4')
        if type(self.deck) != list:
            raise TypeError("deck needs to be a list type of array")

    def cards_shuffle(self):
        """shuffle the deck"""
        if self.deck == []:
            raise ValueError("can't shuffle an empty deck")
        random.shuffle(self.deck)
        if self.deck == random.shuffle:
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
