class Item:
    def __init__(self, name, price, quantity):
        print(f"Instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y


item1 = Item('phone', 1200, 5)

item1 = Item('Laptop', 2000, 3)
