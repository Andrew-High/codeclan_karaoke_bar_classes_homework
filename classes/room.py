class Room:
    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.song_library = []
        self.guest_list = []

    def check_song_library(self):
        return len(self.song_library)

    def add_song_to_library(self, song):
        self.song_library.append(song)

    def check_guest_list(self):
        return len(self.guest_list)
    
    def check_guest_into_room(self, guest):
        if self.check_guest_list() >= self.capacity:
            return "I'm sorry but this room is full, please find another room"
        else:
            self.guest_list.append(guest)

    def check_guest_out_of_room(self, guest):
        self.guest_list.remove(guest)

