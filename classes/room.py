class Room:
    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.song_library = []

    def check_song_library(self):
        return len(self.song_library)

    def add_song_to_library(self, song):
        self.song_library.append(song)
