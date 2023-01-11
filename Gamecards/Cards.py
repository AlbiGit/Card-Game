from random import randint
class Cards:
    def __init__(self,cardnum,cardsymbol):
        self.cardnumber = cardnum
        self.cardsymbol = cardsymbol
        self.playeddeck = {}

    def __str__(self):
        if self.cardnumber in range(2, 10):
            return f'The card is {self.cardnumber} of {self.cardsymbol}'
        elif self.cardnumber == 1:
            return f'The card is Ace of {self.cardsymbol}'
        elif self.cardnumber == 11:
            return f'The card is Jack of {self.cardsymbol}'
        elif self.cardnumber == 12:
            return f'The card is Queen of {self.cardsymbol}'
        elif self.cardnumber == 13:
            return f'The card is King of {self.cardsymbol}'
    def card(self,suit):
        self.cardnumber = randint in range (1,13)
        suit = randint in range (1,4)
        if suit == 1:
            return self.cardsymbol == f'Diamond'
        elif suit == 2:
            return self.cardsymbol == f'Spade'
        elif suit == 3:
            return self.cardsymbol == f'Heart'
        else:
            return self.cardsymbol == f'Club'

    def __gt__(self, other):
        if self.card > other.card:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.card == other.card:
            return True
        else:
            return False
print(Cards.card)