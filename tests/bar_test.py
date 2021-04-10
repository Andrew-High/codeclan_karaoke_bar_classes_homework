import unittest

from classes.bar import Bar
from classes.drink import Drink

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar_1 = Bar("The Squealing Pig")
        self.drink_1 = Drink("Punk IPA", "Beer", 4)

    def test_bar_has_name(self):
        self.assertEqual("The Squealing Pig", self.bar_1.bar_name)