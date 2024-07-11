class Item:
    pay_rate = 0.8
    def __init__(self, name, price, quantity):
        # validations
        assert price >= 0, f"Price {price} is less than 0,enter value greater than 0."
        assert quantity >= 1 ,f"Quantity{quantity} is less than 1,enter value greater than 1."
        # print(f"Instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item('phone', 1200, 5)

item2 = Item('Laptop', 2000, 3)
item2.apply_discount()
print(item2.price)