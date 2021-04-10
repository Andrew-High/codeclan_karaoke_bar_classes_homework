class Bar:
    def __init__(self, bar_name):
        self.bar_name = bar_name
        self.stock_list = []

    def add_drink_to_stock(self, drink):
        self.stock_list.append(drink)

    def check_if_drink_is_in_stock(self, drink):
        for item in self.stock_list:
            if item.drink_name == drink.drink_name:
                return f"We have {drink.drink_name} in stock, there are {drink.quantity} in stock"
        else:
            return f"I'm sorry, we don't have {drink.drink_name} in stock"
