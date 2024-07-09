class Item:
    def __init__(self, name, price, quantity):
        # validations
        assert price >= 0
        assert quantity >= 1
        # print(f"Instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item('phone', 1200, 5)

item2 = Item('Laptop', 2000, 3)
print(item1.calculate_total_price())
