import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Freddie Mercury", "Bohemian Rhapsody")

    def test_guest_has_name(self):
        self.assertEqual("Freddie Mercury", self.guest_1.guest_name)