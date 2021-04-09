import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Killer Queen")

    def test_song_has_name(self):
        self.assertEqual("Killer Queen", self.song_1.song_name)