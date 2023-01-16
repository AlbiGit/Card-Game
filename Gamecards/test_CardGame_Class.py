from unittest import TestCase
from Player_Class import Player
from DeckOfCards_Class import DeckOfCards
from CardGame_Class import CardGame
from Card_Class import Card
class TestCardGame(TestCase):
    # Setup for testing CardGame
    def setUp(self):
        self.test_game = CardGame('aviv', 'albert', 26)

    # Testing valid init values strings for player names and an int value for number of cards
    # also tests that the player hand that gets created for each player is a list type
    def test_init_valid(self):
        self.assertEqual('aviv', self.test_game.player_a.player_name)
        self.assertEqual('albert', self.test_game.player_b.player_name)
        self.assertEqual(26, len(self.test_game.player_a.player_hand))
        self.assertEqual(26, len(self.test_game.player_b.player_hand))
        self.assertTrue(type(self.test_game.player_a) == Player)
        self.assertTrue(type(self.test_game.player_b) == Player)
        self.assertTrue(type(self.test_game.player_a.player_hand) == list)
        self.assertTrue(type(self.test_game.player_b.player_hand) == list)

    # Testing invalid player type input for player 1
    def test_init_invalid_name_1(self):
        with self.assertRaises(TypeError):
            self.test_game = CardGame(Player, 'albert', 26)

    # Testing invalid player type input for player 2
    def test_init_invalid_name_2(self):
        with self.assertRaises(TypeError):
            self.test_game = CardGame('aviv', DeckOfCards, 26)

    def test_init_invalid_name_empty(self):
        with self.assertRaises(ValueError):
            self.test_game = CardGame('', 'albert', 26)

    # Testing invalid card amount type input
    def test_init_invalid_cards_amount_type(self):
        with self.assertRaises(TypeError):
            self.test_game = CardGame('aviv', 'albert', 'a lot of cards')

    # Testing invalid card amount value input that geos over max of 26 cards that should turn into 26 cards
    def test_init_invalid_cards_amount_above_max(self):
        self.test_game = CardGame('aviv', 'albert', 27)
        self.assertEqual(26, len(self.test_game.player_a.player_hand))

    # Testing invalid card amount value input that geos under min number of 10 cards that should turn into 26 cards
    def test_init_invalid_cards_amount_2(self):
        self.test_game = CardGame('aviv', 'albert', 9)
        self.assertEqual(26, len(self.test_game.player_a.player_hand))

    # Testing for both players having the same number of cards in their hand but aren't the same hand
    def test_new_game_valid(self):
        self.assertEqual(len(self.test_game.player_a.player_hand), len(self.test_game.player_b.player_hand))
        self.assertNotEqual(self.test_game.player_a.player_hand, self.test_game.player_b.player_hand)

    # Testing for duplicate cards in different hands
    def test_new_game_valid_in_depth(self):
        for i in self.test_game.player_a.player_hand:
            if i in self.test_game.player_b.player_hand:
                return self.fail()
        pass

    # Testing to see if the get winner function gets the correct winner
    def test_get_winner_valid(self):
        self.test_game.player_b.player_hand = [Card(4, 4)]
        self.assertTrue(self.test_game.get_winner() == self.test_game.player_a)

    # Testing to see the get winner function when no player is the winner
    def test_get_winner_valid_draw(self): # player a wins
        self.test_game.player_a.player_hand = [Card(4, 4)]
        self.test_game.player_b.player_hand = [Card(5, 4)]
        self.assertTrue(self.test_game.get_winner() == None)