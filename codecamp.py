class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name, price, quantity):
        # validations
        assert price >= 0, f"Price {price} is less than 0,enter value greater than 0."
        assert quantity >= 1 ,f"Quantity{quantity} is less than 1,enter value greater than 1."
        # print(f"Instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item('phone', 1200, 5)
item2 = Item('Laptop', 2000, 3)
item3 = Item('printer', 2200, 2)
item4 = Item('cable', 100, 10)
item5 = Item('monitor', 500, 4)

print(Item.__dict__)#all attributes for Class level
print(item2.__dict__)#all attributes for instance level
item1.apply_discount()
print(item1.price)
item5.pay_rate = 0.9
item5.apply_discount()
print(item5.price)
