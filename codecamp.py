import csv
class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity):
        # validations
        assert price >= 0, f"Price {price} is less than 0,enter value greater than 0."
        assert quantity >= 1, f"Quantity{quantity} is less than 1,enter value greater than 1."
        # print(f"Instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_class(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
        




Item.instantiate_from_class()