import unittest

from classes.bar import Bar
from classes.drink import Drink

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar_1 = Bar("The Squealing Pig")
        self.drink_1 = Drink("Punk IPA", "Beer", 5, 4)

    def test_bar_has_name(self):
        self.assertEqual("The Squealing Pig", self.bar_1.bar_name)

    def test_add_drink_to_stock(self):
        self.bar_1.add_drink_to_stock(self.drink_1)
        self.assertEqual("We have Punk IPA in stock, there are 4 in stock", self.bar_1.check_if_drink_is_in_stock(self.drink_1))