import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Lizard Lounge", 4, 10)
        self.song_1 = Song("Killer Queen")
        self.guest_1 = Guest("Freddie Mercury", "Killer Queen", 30)
        self.guest_2 = Guest("Paul McCartney", "Live and Let Die", 100)
        self.guest_3 = Guest("Axl Rose", "Sweet Child of Mine", 10)
        self.guest_4 = Guest("Jon Bon Jovi", "Livin' on a Prayer", 40)
        self.guest_5 = Guest("Michael Jackson", "Billie Jean", 4000)
        self.guest_6 = Guest("Annie Lennox", "Sweet Dreams", 5)

    def test_room_has_name(self):
        self.assertEqual("Lizard Lounge", self.room_1.room_name)

    def test_add_song_to_library(self):
        self.room_1.add_song_to_library(self.song_1)
        self.assertEqual(1, self.room_1.check_song_library())

    def test_check_guest_into_room(self):
        self.room_1.check_guest_into_room(self.guest_1)
        self.assertEqual(1, self.room_1.check_guest_list())

    def test_check_guest_out_of_room(self):
        self.room_1.check_guest_into_room(self.guest_1)
        self.room_1.check_guest_out_of_room(self.guest_1)
        self.assertEqual(0, self.room_1.check_guest_list())

    def test_guest_capacity_cannot_be_exceeded(self):
        self.room_1.check_guest_into_room(self.guest_1)
        self.room_1.check_guest_into_room(self.guest_2)
        self.room_1.check_guest_into_room(self.guest_3)
        self.room_1.check_guest_into_room(self.guest_4)
        self.assertEqual("I'm sorry but this room is full, please find another room", self.room_1.check_guest_into_room(self.guest_5))

    def test_guest_entry_fee_paid(self):
        self.room_1.check_guest_into_room(self.guest_1)
        self.assertEqual(20, self.guest_1.wallet)

    def test_when_guest_doesnt_have_enough_in_wallet_for_entry_fee(self):
        self.assertEqual("I'm sorry but you don't have enough money to pay the entry fee", self.room_1.check_guest_into_room(self.guest_6))

    def test_how_much_guests_have_spent(self):
        self.room_1.check_guest_into_room(self.guest_1)
        self.room_1.check_guest_into_room(self.guest_2)
        self.room_1.check_guest_into_room(self.guest_3)
        self.assertEqual(30, self.room_1.how_much_guests_have_spent())
