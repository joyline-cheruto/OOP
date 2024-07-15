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
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            try:
                name = item.get('name', 'Unknown')
                price = float(item.get('price', 0))
                quantity = item.get('quantity')
                if quantity is None:
                    quantity = 0
                else:
                    quantity = int(quantity)

                # Only instantiate Item if quantity is greater than 0
                if quantity > 0:
                    cls(name=name, price=price, quantity=quantity)
                else:
                    print(f"Skipping item {name} with non-positive quantity: {quantity}")
            except ValueError as e:
                print(f"Error converting values for item {item}: {e}")
            except TypeError as e:
                print(f"Type error for item {item}: {e}")

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


Item.instantiate_from_class()
print(Item.all)
