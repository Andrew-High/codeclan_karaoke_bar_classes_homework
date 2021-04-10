class Guest:
    def __init__(self, guest_name, favourite_song, wallet):
        self.guest_name = guest_name
        self.favourite_song = favourite_song
        self.wallet = wallet
        self.currently_singing = []

    def check_if_favourite_song_present(self, room):
        for song in room.song_library:
            if song.song_name == self.favourite_song:
                return f"Yeah! They have {self.favourite_song}, I'm going to sing that!"
        return "Aww, they don't have my favourite song."
