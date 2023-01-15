from unittest import TestCase
from unittest.mock import MagicMock
import Player_Class
from DeckOfCards_Class import DeckOfCards
from Card_Class import Card
from unittest.mock import patch

class TestPlayer(TestCase):
    def setUp(self): #setting up diffrent players to call onto later
        self.player1 = Player_Class.Player("a",10) #min values
        self.player2 = Player_Class.Player("yugi",15) #mid values
        self.player3 = Player_Class.Player("Esteban Julio Ricardo Montoya De la Rosa Ramirez",26) #max values note that the player name has no max value or illigel charecters only requierment is its a string value
        self.decktest = DeckOfCards()
        self.cardtest = Card(4, 4)


    def test__init__player_names_valid(self): # valid init player name testing
        self.assertEqual("a", self.player1.player_name)
        self.assertEqual("yugi", self.player2.player_name)
        self.assertEqual("Esteban Julio Ricardo Montoya De la Rosa Ramirez", self.player3.player_name)
    def test__init__player_names_invalid(self): # invalid name tests
        with self.assertRaises(TypeError):
            player = Player_Class.Player(10, 10)
        with self.assertRaises(ValueError):
            player = Player_Class.Player("", 10)
    def test__init__player_hand_valid_type(self): #test valid player hands
        self.assertEqual(list, type(self.player1.player_hand))
    def test__init__player_hand_invalid_type(self): #test for an invalid type'
        with self.assertRaises(TypeError):
            player = Player_Class.Player('frank', "10")

    def test__init__player_card_amount_Valid(self):
        self.assertEqual(10, self.player1.cards_amount)
        self.assertEqual(15, self.player2.cards_amount)
        self.assertEqual(26, self.player3.cards_amount)

    def test__init__player_card_amount_Invalid_type(self):
        with self.assertRaises(TypeError):
            cards = Player_Class.Player("jeff", "10")

    def test__init__player_card_invalid_amount(self):
        """checks if the program set default as 26"""
        self.player1 = Player_Class.Player("a", 9)
        self.assertEqual(26, self.player1.cards_amount)
        self.player1 = Player_Class.Player("a", -9)
        self.assertEqual(26, self.player1.cards_amount)
        self.player1 = Player_Class.Player("a", 27)
        self.assertEqual(26, self.player1.cards_amount)


    def test_set_hand_valid_len(self):
        self.player1.set_hand(self.decktest)
        self.assertEqual(10, len(self.player1.player_hand))
        self.player2.set_hand(self.decktest)
        self.assertEqual(15, len(self.player2.player_hand))
        self.player3.set_hand(self.decktest)
        self.assertEqual(26, len(self.player3.player_hand))
    def test_set_hand_valid_type(self):
        self.player1.set_hand(self.decktest)
        self.assertTrue(10, len(self.player1.player_hand))
        self.assertTrue(type(self.player1.player_hand) == list)

    def test_set_hand_invalid_deck_type(self):
        """checks invalid deck type"""
        with self.assertRaises(TypeError):
            self.player1.set_hand('deck')
            deck = []
            self.player1.set_hand(deck)

    def test_get_card_valid(self):
        """checks if func returns card"""
        self.player1.set_hand(self.decktest)
        self.assertTrue(type(self.player1.get_card()) == Card)

    def test_get_card_valid_last_card(self):
        """get last card"""
        self.player1.player_hand = [Card(10, 1)]
        self.assertEqual(self.player1.get_card(), Card(10, 1))
        self.assertEqual(len(self.player1.player_hand), 0)

    def test_get_card_valid_no_card(self):
        """empty hand"""
        self.player1.player_hand = []
        self.assertEqual(len(self.player1.player_hand), 0)
        self.assertEqual(self.player1.get_card(), None)

    def test_get_card_valid_len(self):
        """checks if the len changes after get_card"""
        self.player1.set_hand(self.decktest)
        hand_len = len(self.player1.player_hand)
        self.player1.get_card()
        self.assertEqual(len(self.player1.player_hand), hand_len - 1)

    def test_add_card_valid_len(self):
        """checks if the len changes after add_card"""
        hand_len = len(self.player1.player_hand)
        self.player1.add_card(self.cardtest)
        self.assertEqual(len(self.player1.player_hand), hand_len + 1)

    def test_add_card_invalid_card_type(self):
        """checks adding invalid card type"""
        with self.assertRaises(TypeError):
            self.player1.add_card("card")

    def test_add_card_invalid_value_type(self):
        """checks invalid suit type"""
        with self.assertRaises(TypeError):
            self.cardtest = Card('ten', 4)
            self.player1.add_card(self.cardtest)

    def test_add_card_invalid_suit_type(self):
        """checks invalid suit type"""
        with self.assertRaises(TypeError):
            self.cardtest = Card(10, 'Spades')
            self.player1.add_card(self.cardtest)

    def test_add_card_invalid_value_14(self):
        """checks invalid card value"""
        with self.assertRaises(ValueError):
            self.cardtest = Card(14, 4)
            self.player1.add_card(self.cardtest)

    def test_add_card_invalid_value_0(self):
        """checks invalid card value"""
        with self.assertRaises(ValueError):
            self.cardtest = Card(0, 4)
            self.player1.add_card(self.cardtest)

    def test_add_card_invalid_value_negative(self):
        """checks invalid card value"""
        with self.assertRaises(ValueError):
            self.cardtest = Card(-5, 4)
            self.player1.add_card(self.cardtest)

    def test_add_card_invalid_suit_5(self):
        """checks invalid card suit"""
        with self.assertRaises(ValueError):
            self.cardtest = Card(10, 5)
            self.player1.add_card(self.cardtest)

    def test_add_card_invalid_suit_0(self):
        """checks invalid card suit"""
        with self.assertRaises(ValueError):
            self.cardtest = Card(10, 0)
            self.player1.add_card(self.cardtest)

    def test_add_card_invalid_suit_negative(self):
        """checks invalid card suit"""
        with self.assertRaises(ValueError):
            self.cardtest = Card(10, -4)
            self.player1.add_card(self.cardtest)


