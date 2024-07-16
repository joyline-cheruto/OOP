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
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_an_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


class Phone(Item):
    all = []
    def __init__(self, name:str, price:float, quantity = 0 ,brokenPhones = 0):
        # validations
        assert price >= 0, f"Price {price} is less than 0,enter value greater than 0."
        assert quantity >= 1, f"Quantity{quantity} is less than 1,enter value greater than 1."
        assert brokenPhones >= 1, f"Quantity{brokenPhones} is less than 1,enter value greater than 1."
        # print(f"Instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.brokenPhones = brokenPhones

        Phone.all.append(self)


phone1 = Phone("Tecno", 500, 4,1)
print(phone1.calculate_total_price())
phone2 = Phone("Samsung", 600, 8,1)

