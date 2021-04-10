import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.bar import Bar
from classes.drink import Drink

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Freddie Mercury", "Killer Queen", 30)
        self.guest_2 = Guest("Axl Rose", "Sweet Child of Mine", 10)
        self.room_1 = Room("Lizard Lounge", 4, 10)
        self.song_1 = Song("Killer Queen")
        self.bar_1 = Bar("The Squealing Pig")
        self.drink_1 = Drink("Punk IPA", "Beer", 5, 4)

    def test_guest_has_name(self):
        self.assertEqual("Freddie Mercury", self.guest_1.guest_name)

    def test_guest_favourite_song(self):
        self.assertEqual("Killer Queen", self.guest_1.favourite_song)

    def test_response_when_favourite_song_present_in_song_library(self):
        self.room_1.add_song_to_library(self.song_1)
        self.room_1.check_guest_into_room(self.guest_1)
        self.assertEqual("Yeah! They have Killer Queen, I'm going to sing that!", self.guest_1.check_if_favourite_song_present(self.room_1))

    def test_customer_can_buy_drink_from_bar(self):
        self.room_1.check_guest_into_room(self.guest_1)
        self.bar_1.add_drink_to_stock((self.drink_1))
        self.guest_1.buy_drink(self.drink_1, self.bar_1, self.room_1)
        self.assertEqual(15, self.guest_1.wallet)

    def test_customer_cant_buy_drink_from_bar(self):
        self.room_1.check_guest_into_room(self.guest_2)
        self.bar_1.add_drink_to_stock((self.drink_1))
        self.guest_2.buy_drink(self.drink_1, self.bar_1, self.room_1)
        self.assertEqual(0, self.guest_2.wallet)
        self.assertEqual("We have Punk IPA in stock, there are 4 in stock", self.bar_1.check_if_drink_is_in_stock(self.drink_1))