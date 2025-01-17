import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity):
        # validations
        assert price >= 0, f"Price {price} is less than 0,enter value greater than 0."
        assert quantity >= 1, f"Quantity{quantity} is less than 1,enter value greater than 1."
        # print(f"Instance created: {name}")
        self._name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)
    @property
    def price(self):
        return self.__price

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value
    @property
    def name(self):
        print("trying to get name")
        return self._name

    @name.setter
    def name(self, value):
        print("trying to set name")
        self._name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

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
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

    def __connect(self,smpt_server):
        pass
    def __prepare_body(self):
        return f"Hello,You got {self.pay_rate} discount."
    def __send(self):
        pass
    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()