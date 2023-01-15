class Card:
    # Setup for the Card class for what inputs it accepts to create a new card with a value and suit
    def __init__(self, card_number, card_symbol):
        if type(card_number) != int:
            raise TypeError
        if type(card_symbol) != int:
            raise TypeError
        if not 1 <= card_number <= 13:
            raise ValueError('card value must be between 1 to 13')
        if not 1 <= card_symbol <= 4:
            raise ValueError('card symbol must be between 1 to 4')
        self.card_value = card_number
        self.card_suit = card_symbol

    # Setup for testing what card is greater than the other in value
    def __gt__(self, other):
        if type(other) != Card:
            raise TypeError
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

    # Setup for testing if 2 cards equal to one another by their numeral and suit value
    def __eq__(self, other):
        if [self.card_value, self.card_suit] == [other.card_value, other.card_suit]:
            return True
        else:
            return False

        # Setup string value that's returned for each corresponding value of card
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

    # Setup for repr to return a list of cards
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
