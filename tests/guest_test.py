import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Freddie Mercury", "Killer Queen", 30)

    def test_guest_has_name(self):
        self.assertEqual("Freddie Mercury", self.guest_1.guest_name)

    def test_guest_favourite_song(self):
        self.assertEqual("Killer Queen", self.guest_1.favourite_song)