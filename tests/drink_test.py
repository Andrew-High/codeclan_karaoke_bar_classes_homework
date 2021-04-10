import unittest

from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Punk IPA", "Beer", 5, 4)

    def test_drink_has_name(self):
        self.assertEqual("Punk IPA", self.drink_1.drink_name)