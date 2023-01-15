from unittest import TestCase
from Card_Class import Card
class TestCard(TestCase):
    # Setup for testing the Card class
    def setUp(self):
        self.card1 = Card(13, 4)  # Edge case for max values
        self.card2 = Card(1, 1)  # Edge case for min values
        self.card3 = Card(7, 2)  # Case with middle values
        self.card4 = Card(1, 1)  # Card that is the same as the other for testing EQ

    # Testing valid init values for both suit and numer value
    def test__init__valid(self):
        self.assertEqual(13, self.card1.card_value)
        self.assertEqual(4, self.card1.card_suit)
        self.assertEqual(1, self.card2.card_value)
        self.assertEqual(1, self.card2.card_suit)
        self.assertEqual(7, self.card3.card_value)
        self.assertEqual(2, self.card3.card_suit)

    # Testing if the numeral value exceeds max allowed value
    def test__init__invalid_big_value(self):
        with self.assertRaises(ValueError):
            card = Card(14, 1)

    # Testing if the numeral value is set to 0
    def test__init__invalid_zero_value(self):
        with self.assertRaises(ValueError):
            card = Card(0, 1)

    # Testing if the numeral value is negative
    def test__init__invalid_negative_value(self):
        with self.assertRaises(ValueError):
            card = Card(-14, 1)

    # Testing if the numeral value is the wrong type
    def test__init__invalid_type_value(self):
        with self.assertRaises(TypeError):
            card = Card("Ace", 1)

    # Testing if the suit value exceeds max value
    def test__init__invalid_big_suit(self):
        with self.assertRaises(ValueError):
            card = Card(5, 5)

    # Testing if the suit value is set to 0
    def test__init__invalid_zero_suit(self):
        with self.assertRaises(ValueError):
            card = Card(5, 0)

    # Testing if the suit value is negative
    def test__init__invalid_negative_suit(self):
        with self.assertRaises(ValueError):
            card = Card(5, -1)

    # Testing if the suit value is the wrong type
    def test__init__invalid_type_suit(self):
        with self.assertRaises(TypeError):
            card = Card(12, "spades")

    # Testing Gt to check if it correctly determines the greater card by numeral value then by suit
    def test__gt__Valid(self):
        self.assertTrue(self.card2 > self.card1)  # Testing for greater numeral value
        self.assertTrue(Card(1, 2) > self.card2)  # Testing for greater suit value
        self.assertTrue(self.card2 > Card(13, 1))  # Testing that ace is a greater value than a king

    # Testing that gq won't do a comparison for invalid types
    def test__gt__inValid(self):
        with self.assertRaises(TypeError):
            self.card1 > 12

    # Testing that EQ compares the Values on cards that carry the same numeral and suit value
    def test__eq__Valid(self):
        self.assertTrue(self.card2 == self.card4)

    # Testing that EQ won't compare values to the wrong type
    def test__eq__invalid(self):
        with self.assertRaises(TypeError):
            self.card1 == "King of clubs"
