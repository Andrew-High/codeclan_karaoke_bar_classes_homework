import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Freddie Mercury", "Killer Queen", 30)
        self.room_1 = Room("Lizard Lounge", 4, 10)
        self.song_1 = Song("Killer Queen")

    def test_guest_has_name(self):
        self.assertEqual("Freddie Mercury", self.guest_1.guest_name)

    def test_guest_favourite_song(self):
        self.assertEqual("Killer Queen", self.guest_1.favourite_song)

    def test_response_when_favourite_song_present_in_song_library(self):
        self.room_1.add_song_to_library(self.song_1)
        self.room_1.check_guest_into_room(self.guest_1)
        self.assertEqual("Yeah! They have Killer Queen, I'm going to sing that!", self.guest_1.check_if_favourite_song_present(self.room_1))