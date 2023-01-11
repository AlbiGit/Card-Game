from random import randint
from Gamecards import Cards
class Deck:
    def __init__(self, deck):
        self.deck = []
        deck = self.deck

    def card(self,suit):
        self.cardnumber = randint in range (1,14)
        suit = randint in range (1,4)
        if suit == 1:
            return self.cardsymbol == f'Diamond'
        elif suit == 2:
            return self.cardsymbol == f'Spade'
        elif suit == 3:
            return self.cardsymbol == f'Heart'
        else:
            return self.cardsymbol == f'Club'
    def __repr__(self):
        if self.cardnumber in range(2, 11):
            return f'The card is {self.cardnumber} of {self.cardsymbol}'
        elif self.cardnumber == 1:
            return f'The card is Ace of {self.cardsymbol}'
        elif self.cardnumber == 11:
            return f'The card is Jack of {self.cardsymbol}'
        elif self.cardnumber == 12:
            return f'The card is Queen of {self.cardsymbol}'
        elif self.cardnumber == 13:
            return f'The card is King of {self.cardsymbol}'
    def __str__(self):
        if self.cardnumber in range(2, 11):
            return f'The card is {self.cardnumber} of {self.cardsymbol}'
        elif self.cardnumber == 1:
            return f'The card is Ace of {self.cardsymbol}'
        elif self.cardnumber == 11:
            return f'The card is Jack of {self.cardsymbol}'
        elif self.cardnumber == 12:
            return f'The card is Queen of {self.cardsymbol}'
        elif self.cardnumber == 13:
            return f'The card is King of {self.cardsymbol}'
    def shuffle(self):
        while len(self.deck) < 52:
            card =  Deck.card
             if self.deck.count(card) < 1:
                 self.deck.append(card)
