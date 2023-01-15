from Card_Class import Card
from DeckOfCards_Class import DeckOfCards
import random
class Player:
    def __init__(self, name: str, number_of_cards_to_deal: int):
        """sets a new player"""
        if type(name) != str:
            raise TypeError
        if name == '':
            raise ValueError("the name can't be empty")
        if type(number_of_cards_to_deal) != int:
            raise TypeError('number of cards must be type int')
        if not 10 <= number_of_cards_to_deal <= 26:
            number_of_cards_to_deal = 26
            print("wrong amount, set to default (26)")
        self.player_name = name
        self.player_hand = []
        self.cards_amount = number_of_cards_to_deal

    def set_hand(self, deck: DeckOfCards):
        """sets the player's hand according to the amount of cards entered at the beginning of the game"""
        if type(deck) != DeckOfCards:
            raise TypeError("set_hand takes only DeckOfCards objects")
        for i in range(self.cards_amount):
            card = deck.deal_one()
            self.player_hand.append(card)

    def get_card(self):
        """takes one card out of the player's hand and returns it"""
        if len(self.player_hand) == 0:
            print(f"{self.player_name} has no more cards left")
            return None
        elif len(self.player_hand) == 1:
            card = self.player_hand.pop(0)
            print("that was the last card, no more cards left")
        else:
            card = self.player_hand.pop(random.randint(0, len(self.player_hand) - 1))
        return card

    def add_card(self, card: Card):
        """adds a card to the player's hand"""
        if type(card) != Card:
            raise TypeError('add_card can only append objects of Card type')
        if type(card.card_value) != int:
            raise TypeError
        if type(card.card_suit) != int:
            raise TypeError
        if not 1 <= card.card_value <= 13:
            raise ValueError('card value must be between 1 to 13')
        if not 1 <= card.card_suit <= 4:
            raise ValueError('card symbol must be between 1 to 4')

        self.player_hand.append(card)
