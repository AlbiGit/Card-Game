from unittest import TestCase
from Player_Class import Player
from DeckOfCards_Class import DeckOfCards
from Card_Class import Card
from CardGame_Class import CardGame


class TestCardGame(TestCase):
    def setUp(self):
        self.test_game = CardGame('aviv', 'albert', 26)

    def test_init_valid(self):
        self.assertEqual('aviv', self.test_game.player_a.player_name)
        self.assertEqual('albert', self.test_game.player_b.player_name)
        self.assertEqual(26, len(self.test_game.player_a.player_hand))
        self.assertEqual(26, len(self.test_game.player_b.player_hand))
        self.assertTrue(type(self.test_game.player_a) == Player)
        self.assertTrue(type(self.test_game.player_b) == Player)
        self.assertTrue(type(self.test_game.player_a.player_hand) == list)
        self.assertTrue(type(self.test_game.player_b.player_hand) == list)

    def test_init_invalid_name_1(self):
        with self.assertRaises(TypeError):
            self.test_game = CardGame(Player, 'albert', 26)

    def test_init_invalid_name_2(self):
        with self.assertRaises(TypeError):
            self.test_game = CardGame('aviv', DeckOfCards, 26)

    def test_init_invalid_cards_amount_type(self):
        with self.assertRaises(TypeError):
            self.test_game = CardGame('aviv', 'albert', 'a lot of cards')

    def test_init_invalid_cards_amount_1(self):
        self.test_game = CardGame('aviv', 'albert', 27)
        self.assertEqual(26, len(self.test_game.player_a.player_hand))

    def test_init_invalid_cards_amount_2(self):
        self.test_game = CardGame('aviv', 'albert', 9)
        self.assertEqual(26, len(self.test_game.player_a.player_hand))
    def test_new_game(self):
        pass
    def test_get_winner(self):
        pass
