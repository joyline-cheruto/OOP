class Item:
    def __init__(self,name):
        print(f"Instance created: {name}")
        self.name = name
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item('phone')
item1.price = 1200
item1.quantity = 5

item1 = Item('Laptop')
item1.price = 1200
item1.quantity = 5