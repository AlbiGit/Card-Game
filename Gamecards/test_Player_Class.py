from unittest import TestCase
import Player_Class
from DeckOfCards_Class import DeckOfCards
from Card_Class import Card
class TestPlayer(TestCase):
    # Setup for testing Player
    # Note that for the player name the only requirement is that the name isn't left a blank and is a string value
    def setUp(self):
        self.player1 = Player_Class.Player("a", 10)  # Edge case with minimal valid values
        self.player2 = Player_Class.Player("yugi", 15)  # Mid values
        self.player3 = Player_Class.Player("Esteban Julio Ricardo Montoya De la Rosa Ramirez", 26)  # Max valid values
        self.decktest = DeckOfCards()
        self.cardtest = Card(4, 4)

    # Testing valid init of player names
    def test__init__player_names_valid(self):
        self.assertEqual("a", self.player1.player_name)
        self.assertEqual("yugi", self.player2.player_name)
        self.assertEqual("Esteban Julio Ricardo Montoya De la Rosa Ramirez", self.player3.player_name)

    # Testing invalid player names
    def test__init__player_names_invalid(self):
        with self.assertRaises(TypeError):
            Player_Class.Player(10, 10)
        with self.assertRaises(ValueError):
            Player_Class.Player("", 10)

    # Testing valid player hands type
    def test__init__player_hand_valid_type(self):
        self.assertEqual(list, type(self.player1.player_hand))

    # Testing valid init player hand amounts
    def test__init__player_card_amount_Valid(self):
        self.assertEqual(10, self.player1.cards_amount)
        self.assertEqual(15, self.player2.cards_amount)
        self.assertEqual(26, self.player3.cards_amount)

    # Testing invalid player hand card amount type
    def test__init__player_card_amount_Invalid_type(self):
        with self.assertRaises(TypeError):
            Player_Class.Player("jeff", "10")

    # Testing invalid player card amount value to see if the value goes over 26 or under 9 it sets the card amount to 26
    def test__init__player_card_invalid_amount(self):
        """checks if the program set default as 26"""
        self.player1 = Player_Class.Player("a", 9)
        self.assertEqual(26, self.player1.cards_amount)
        self.player1 = Player_Class.Player("a", -9)
        self.assertEqual(26, self.player1.cards_amount)
        self.player1 = Player_Class.Player("a", 27)
        self.assertEqual(26, self.player1.cards_amount)

    # Testing valid player hand lengths
    def test_set_hand_valid_len(self):
        self.player1.set_hand(self.decktest)
        self.assertEqual(10, len(self.player1.player_hand))
        self.player2.set_hand(self.decktest)
        self.assertEqual(15, len(self.player2.player_hand))
        self.player3.set_hand(self.decktest)
        self.assertEqual(26, len(self.player3.player_hand))

    # Testing that the set hand function sets it to the valid type
    def test_set_hand_valid_type(self):
        self.player1.set_hand(self.decktest)
        self.assertTrue(10, len(self.player1.player_hand))
        self.assertTrue(type(self.player1.player_hand) == list)

    # Testing set hand invalid deck type
    def test_set_hand_invalid_deck_type(self):
        with self.assertRaises(TypeError):
            self.player1.set_hand('deck')
            deck = []
            self.player1.set_hand(deck)

    # Testing valid get card function that it returns a card type variable for the players hand
    def test_get_card_valid(self):
        self.player1.set_hand(self.decktest)
        self.assertTrue(type(self.player1.get_card()) == Card)

    # Testing that the get card function can get the last card from the players hand
    def test_get_card_valid_last_card(self):
        self.player1.player_hand = [Card(10, 1)]
        self.assertEqual(self.player1.get_card(), Card(10, 1))
        self.assertEqual(len(self.player1.player_hand), 0)

    # Testing that the get card function won't get a card from an empty players hand
    def test_get_card_valid_no_card(self):
        self.player1.player_hand = []
        self.assertEqual(len(self.player1.player_hand), 0)
        self.assertEqual(self.player1.get_card(), None)

    # Testing that the players hand updates with the new number of cards after getting the card from his hand
    def test_get_card_valid_len(self):
        self.player1.set_hand(self.decktest)
        hand_len = len(self.player1.player_hand)
        self.player1.get_card()
        self.assertEqual(len(self.player1.player_hand), hand_len - 1)

    # Testing that the players hand updates with the new number of cards after adding a card to his hand
    def test_add_card_valid_len(self):
        hand_len = len(self.player1.player_hand)
        self.player1.add_card(self.cardtest)
        self.assertEqual(len(self.player1.player_hand), hand_len + 1)

    # Testing tying to add an invalid type to a players hand
    def test_add_card_invalid_card_type(self):
        with self.assertRaises(TypeError):
            self.player1.add_card("card")
