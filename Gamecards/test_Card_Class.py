from unittest import TestCase
from Card_Class import Card
from Gamecards import DeckOfCards_Class
class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card(13, 4)  # מקרה קצה מספר גדול סוג גדול
        self.card2 = Card(1, 1)  # מקרה קצה מספר קטן סוג קטן
        self.card3 = Card(7, 2)  # מקרה אמצע

    def test__init__valid(self):
        """test a valid init"""
        self.assertEqual(13, self.card1.card_value)
        self.assertEqual(4, self.card1.card_suit)
        self.assertEqual(1, self.card2.card_value)
        self.assertEqual(1, self.card2.card_suit)
    def test__init__invalid_big_value(self):
        with self.assertRaises(ValueError):
            card = Card(14, 1)

    def test__init__invalid_small_value(self):
        with self.assertRaises(ValueError):
            card = Card(0, 1)

    def test__init__invalid_negativ_value(self):
        with self.assertRaises(ValueError):
            card = Card(-14, 1)

    def test__init__invalid_type_value(self):
        with self.assertRaises(TypeError):
            card = Card("ace", 1)

    def test__init__invalid_big_suit(self):
        with self.assertRaises(ValueError):
            card = Card(5, 5)

    def test__init__invalid_small_suit(self):
        with self.assertRaises(ValueError):
            card = Card(5, 0)

    def test__init__invalid_negativ_suit(self):
        with self.assertRaises(ValueError):
            card = Card(5, -1)

    def test__init__invalid_type_suit(self):
        with self.assertRaises(TypeError):
            card = Card(12, "spades")


