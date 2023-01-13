from unittest import TestCase
from unittest import mock
from DeckOfCards_Class import DeckOfCards
from CardGame_Class import CardGame
from Card_Class import Card
import random


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.decktest = DeckOfCards()
    def test__init__valid_len(self):
        """checks length of deck when init"""
        self.assertEqual(len(self.decktest.deck), 52)

    def test__init__valid_type(self):
        """checks type of deck"""
        self.assertEqual(type(self.decktest.deck), list)

    def test_cards_shuffle_valid_len(self):
        """checks that the length of the deck doesn't change while shuffling"""
        self.copy_deck = self.decktest.deck.copy()
        self.decktest.cards_shuffle()
        self.assertEqual(len(self.decktest.deck), len(self.copy_deck))

    def test_cards_shuffle_valid_type(self):
        """checks the deck is a list"""
        self.decktest.cards_shuffle()
        self.assertEqual(type(self.decktest.deck), list)

    def test_cards_shuffle_valid_different_list(self):
        """checks that the shuffled deck is different from before shuffling"""
        self.copy_deck = self.decktest.deck.copy()
        self.decktest.cards_shuffle()
        self.assertTrue(self.decktest.deck != self.copy_deck)

    def test_cards_shuffle_invalid_no_cards(self):
        """checks what happens if the deck is empty"""
        with self.assertRaises(ValueError):
            self.decktest.deck = []
            self.decktest.cards_shuffle()

    def test_deal_one_valid_len(self):
        """checks if the length is smaller by one card after dealing"""
        self.copy_deck = self.decktest.deck.copy()
        self.decktest.deal_one()
        self.assertEqual(len(self.copy_deck) - 1, len(self.decktest.deck))

    def test_deal_one_invalid_empty_deck(self):
        self.decktest.deck = []
        self.decktest.deal_one()
        self.assertTrue(self.decktest.deck == [])

    def test_deal_one_valid_card_type(self):
        """checks the type of the returned object"""
        dealed_card = self.decktest.deal_one()
        self.assertTrue(type(dealed_card) == Card)

    def test_deal_one_valid_last_card(self):
        self.decktest.deck = [Card(5, 4)]
        dealed_card = self.decktest.deal_one()
        self.assertEqual(Card(5, 4), dealed_card)





