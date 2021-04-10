class Guest:
    def __init__(self, guest_name, favourite_song, wallet):
        self.guest_name = guest_name
        self.favourite_song = favourite_song
        self.wallet = wallet

    def check_if_favourite_song_present(self, room):
        for song in room.song_library:
            if song.song_name == self.favourite_song:
                return f"Yeah! They have {self.favourite_song}, I'm going to sing that!"
        return "Aww, they don't have my favourite song."

    def buy_drink(self, drink, bar, room):
        for item in bar.stock_list:
            if item.drink_name == drink.drink_name and self.wallet >= drink.price:
                self.wallet = self.wallet - drink.price
                item.quantity -= 1
                room.current_spend += drink.price
        if drink.drink_name in bar.stock_list:
            return "I'm sorry, you don't have enough funds"
        elif self.wallet >= drink.price:
            return f"I'm sorry, we don't have any {drink.drink_name} in stock at the moment, please choose another drink"
            
        