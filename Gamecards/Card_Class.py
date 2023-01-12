class Card:
    def __init__(self, card_number, card_symbol):
        """create a new card with value and suit"""
        self.card_value = card_number
        self.card_suit = card_symbol

    def __gt__(self, other):
        """compair between two cards' value"""
        if self.card_value == 1:
            if other.card_value != 1:
                return True
            elif self.card_value and other.card_value == 1:
                if self.card_suit > other.card.suit:
                    return True
                else:
                    return False
            else:
                return False
        elif self.card_value > other.card_value:
            return True
        elif self.card_value == other.card_value:
            if self.card_suit > other.card.suit:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        """check if cards are equal based on value and suit"""
        if [self.card_value, self.card_suit] == [other.card_value, other.card_suit]:
            return True
        else:
            return False

    # def __str__(self):
    #     # suit = int(self.card_suit)
    #     # if suit == 1:
    #     #     return suit == f'Diamond'
    #     # elif suit == 2:
    #     #     return suit == f'Spade'
    #     # elif suit == 3:
    #     #     return suit == f'Heart'
    #     # else:
    #     #     return suit == f'Club'
    #     #
    #     # if int(self.card_value) in range (2,10):
    #     #     return f'The card is {self.cardnumber} of {suit}'
    #     # elif self.card_value == 1:
    #     #     return f'The card is Ace of {suit}'
    #     # elif self.card_value == 11:
    #     #     return f'The card is Jack of {suit}'
    #     # elif self.card_value == 12:
    #     #     return f'The card is Queen of {suit}'
    #     # else:
    #     #     return f'The card is King of {suit}'
    def __repr__(self):
        suit = int(self.card_suit)
        if suit == 1:
            return suit == f'Diamond'
        elif suit == 2:
            return suit == f'Spade'
        elif suit == 3:
            return suit == f'Heart'
        else:
            return suit == f'Club'

        if int(self.card_value) in range (2,10):
            return f'The card is {self.cardnumber} of {suit}'
        elif self.card_value == 1:
            return f'The card is Ace of {suit}'
        elif self.card_value == 11:
            return f'The card is Jack of {suit}'
        elif self.card_value == 12:
            return f'The card is Queen of {suit}'
        else:
            return f'The card is King of {suit}'
