from unittest import TestCase
from unittest.mock import MagicMock
import Player_Class
from unittest.mock import patch

class TestPlayer(TestCase):
    def setUp(self): #setting up diffrent players to call onto later
        self.player1 = Player_Class.Player("a",10) #min values
        self.player2 = Player_Class.Player("yugi",15) #mid values
        self.player3 = Player_Class.Player("Esteban Julio Ricardo Montoya De la Rosa Ramirez",26) #max values note that the player name has no max value or illigel charecters only requierment is its a string value

    def test__init__player_names_valid(self): #valid init player name testing
        self.assertEqual("a", self.player1.player_name)
        self.assertEqual("yugi", self.player2.player_name)
        self.assertEqual("Esteban Julio Ricardo Montoya De la Rosa Ramirez", self.player3.player_name)
    def test__init__player_names_invalid(self): #invalid name tests
        with self.assertRaises(TypeError):
            player = Player_Class.Player(10,10)
        with self.assertRaises(ValueError):
            player = Player_Class.Player("",10)
    def test__init__player_hand_valid_type(self): #test valid player hands
        self.assertEqual(list,type(self.player1.player_hand))
    def test__init__player_hand_invalid_type(self): #test for an invalid type'
        with self.assertRaises(TypeError):
            player = Player_Class.Player('frank',"10")

    def test__init__player_card_amount_Valid(self):
        self.assertEqual(10,self.player1.cards_amount)
        self.assertEqual(15,self.player2.cards_amount)
        self.assertEqual(26,self.player3.cards_amount)

    def test__init__player_card_amount_Invalid(self):
        with self.assertRaises(TypeError):
            cards = Player_Class.Player("jeff","10")

    def test_set_hand_valid(self):
        pass