class Card:
    def __init__(self, card_number: int, card_symbol):
        """create a new card with value and suit"""
        self.card_value = card_number
        self.card_suit = card_symbol

    def __gt__(self, other):
        """compair between two cards' value"""
        if self.card_value > other.card_value:
            return True
        else:
            return False

    def __eq__(self, other):
        """check if cards are equal based on value and suit"""
        if [self.card_value, self.card_suit] == [other.card_value, other.card_suit]:
            return True
        else:
            return False


    def __str__(self):
        if self.card_suit == 1:
            self.card_suit = 'Diamond'
        if self.card_suit == 2:
            self.card_suit = 'Spades'
        if self.card_suit == 3:
            self.card_suit = 'Heart'
        if self.card_suit == 4:
            self.card_suit = 'Club'
        return f"the card is {self.card_value} of {self.card_suit}"

    def __repr__(self):
        return

card1 = Card(5, 4)
card2 = Card(12, 2)
card3 = Card(7, 1)
cards = [card1, card2, card3]
print(card1)
print(card2)
print(card3)