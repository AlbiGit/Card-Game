from unittest import TestCase
from DeckOfCards_Class import DeckOfCards
from Card_Class import Card
class TestDeckOfCards(TestCase):
    # Setup for testing DeckOfCards
    def setUp(self):
        self.decktest = DeckOfCards()

    # Testing that the deck length won't exceed 52 cards when initialized
    def test__init__valid_len(self):
        self.assertEqual(len(self.decktest.deck), 52)

    # Testing that the deck created is of the correct type
    def test__init__valid_type(self):
        self.assertEqual(type(self.decktest.deck), list)

    # Testing that the shuffled deck stays the same length after shuffling
    def test_cards_shuffle_valid_len(self):
        self.copy_deck = self.decktest.deck.copy()
        self.decktest.cards_shuffle()
        self.assertEqual(len(self.decktest.deck), len(self.copy_deck))

    # Testing that the shuffled deck is of the correct type
    def test_cards_shuffle_valid_type(self):
        self.decktest.cards_shuffle()
        self.assertEqual(type(self.decktest.deck), list)

    # Testing that the shuffled deck gets shuffled into a new order of cards
    # and won't get shuffled back into the starting order
    def test_cards_shuffle_valid_different_list(self):
        self.copy_deck = self.decktest.deck.copy()
        self.decktest.cards_shuffle()
        self.assertTrue(self.decktest.deck != self.copy_deck)

    # Testing for value error when a deck has no cards to shuffle in it
    def test_cards_shuffle_invalid_no_cards(self):
        with self.assertRaises(ValueError):
            self.decktest.deck = []
            self.decktest.cards_shuffle()

    # Testing that deal one removes the card from the deck after dealing it and decreasing the deck length
    def test_deal_one_valid_len(self):
        self.copy_deck = self.decktest.deck.copy()
        self.decktest.deal_one()
        self.assertEqual(len(self.copy_deck) - 1, len(self.decktest.deck))

    # Testing that the deal one function one deal any cards if the deck is empty
    def test_deal_one_invalid_empty_deck(self):
        self.decktest.deck = []
        self.decktest.deal_one()
        self.assertTrue(self.decktest.deck == [])

    # Testing that the deal one function deals a valid card type of variable
    def test_deal_one_valid_card_type(self):
        dealed_card = self.decktest.deal_one()
        self.assertTrue(type(dealed_card) == Card)

    # Testing that the deal one function deals the last card correctly from the deck
    def test_deal_one_valid_last_card(self):
        self.decktest.deck = [Card(5, 4)]
        dealed_card = self.decktest.deal_one()
        self.assertEqual(Card(5, 4), dealed_card)





