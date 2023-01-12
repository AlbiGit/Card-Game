import random
class Card:
    def __init__(self, card_number, card_symbol):
        """create a new card with value and suit"""
        self.card_value = card_number
        self.card_suit = card_symbol

    def __gt__(self, other):
        """compare between two cards value and suit"""
        if self.card_value == 1:
            if other.card_value != 1:
                return True
            elif self.card_value and other.card_value == 1:
                if self.card_suit > other.card_suit:
                    return True
                else:
                    return False
        if self.card_value > other.card_value:
            return True
        if self.card_value == other.card_value:
            if self.card_suit > other.card_suit:
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
    def __str__(self):
        suit = self.card_suit
        val = self.card_value
        if suit == 1:
            suit = 'Diamonds'
        if suit == 2:
            suit = 'Spades'
        if suit == 3:
            suit = 'Hearts'
        if suit == 4:
            suit = 'Clubs'
        if val == 1:
            val = 'Ace'
        if val == 11:
            val = 'Jack'
        if val == 12:
            val = 'Queen'
        if val == 13:
            val = 'King'
        return f"{val} of {suit}"
    def __repr__(self):
        suit = self.card_suit
        val = self.card_value
        if suit == 1:
            suit = 'Diamonds'
        if suit == 2:
            suit = 'Spades'
        if suit == 3:
            suit = 'Hearts'
        if suit == 4:
            suit = 'Clubs'
        if val == 1:
            val = 'Ace'
        if val == 11:
            val = 'Jack'
        if val == 12:
            val = 'Queen'
        if val == 13:
            val = 'King'
        return f"{val} of {suit}"