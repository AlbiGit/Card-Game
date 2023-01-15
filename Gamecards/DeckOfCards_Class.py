from Card_Class import Card
import random
class DeckOfCards:
    # Setup for the DeckOfCards that initializes a deck of cards list with 52 cards when called upon
    def __init__(self):
        self.deck = []
        for suit in [1, 2, 3, 4]:
            for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                self.deck.append(Card(value, suit))
        if len(self.deck) != 52:
            raise ValueError("Deck must be 52 cards")
        if type(self.deck) != list:
            raise TypeError("deck needs to be a list type of array")

    # Card shuffle function that uses the deck that was made and shuffles the cards
    # if for some reason the deck shuffles to the exact same layout it is reshuffled
    def cards_shuffle(self):
        if self.deck == []:
            raise ValueError("can't shuffle an empty deck")
        # makes a copy of the deck
        copy_deck = self.deck.copy()
        random.shuffle(self.deck)
        # after the shuffle, checks that the new order is different from before the shuffle
        while self.deck == copy_deck:
            random.shuffle(self.deck)

    # Deal one function when called upon uses the shuffled deck and deal one card to a player
    # by adding it to his hand whilst simultaneously removing it for the shuffled deck
    # no copies of the same card can be dealt
    def deal_one(self):
        if len(self.deck) == 0:
            print(f"deck has no more cards left")
            return None
        elif len(self.deck) == 1:
            card = self.deck.pop(0)
            return card
        else:
            card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        return card
