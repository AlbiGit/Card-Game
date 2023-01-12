class Card:
    def __init__(self, card_number: int, card_symbol):
        self.card_value = card_number
        self.card_suit = card_symbol

    def __gt__(self, other):
        if self.card_value > other.card_value:
            return True
        else:
            return False

    def __eq__(self, other):
        if [self.card_value, self.card_suit] == [other.card_value, other.card_suit]:
            return True
        else:
            return False