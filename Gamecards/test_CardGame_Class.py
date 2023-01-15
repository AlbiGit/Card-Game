from unittest import TestCase
from Player_Class import Player
from DeckOf Cards_Class import DeckOfCards
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
    def test_new_game_valid(self):
        """checks that both players have same amount of cards and different cards each"""
        self.assertEqual(len(self.test_game.player_a.player_hand), len(self.test_game.player_b.player_hand))
        self.assertNotEqual(self.test_game.player_a.player_hand, self.test_game.player_b.player_hand)

    def test_new_game_valid_in_depth(self):
        """check that none of the cards appears in both hands"""
        for i in self.test_game.player_a.player_hand:
            if i in self.test_game.player_b.player_hand:
                return self.fail()
        pass

    def test_get_winner_valid(self): # player a wins
        """checks if get_winner gets the actual winner"""
        self.test_game.player_b.player_hand = [Card(4, 4)]
        self.assertTrue(self.test_game.get_winner() == self.test_game.player_a)

    def test_get_winner_valid_draw(self): # player a wins
        self.test_game.player_a.player_hand = [Card(4, 4)]
        self.test_game.player_b.player_hand = [Card(5, 4)]
        self.assertTrue(self.test_game.get_winner() == None)




