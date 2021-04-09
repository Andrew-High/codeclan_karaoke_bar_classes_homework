import unittest

from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Lizard Lounge", 6)
        self.song_1 = Song("Killer Queen")

    def test_room_has_name(self):
        self.assertEqual("Lizard Lounge", self.room_1.room_name)