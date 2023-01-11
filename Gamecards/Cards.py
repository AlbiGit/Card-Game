import from Gamecards import Deck
class Cards:
    def __init__(self,cardnum,cardsymbol):
        self.cardnumber = cardnum
        self.cardsymbol = cardsymbol
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