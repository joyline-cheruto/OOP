from Items import Item
class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, brokenPhones=0):
        #call super function to access all attributes and methods
        super().__init__(
            name, price, quantity
        )
        # validations
        assert brokenPhones >= 1, f"Quantity{brokenPhones} is less than 1,enter value greater than 1."
        # print(f"Instance created: {name}")

        self.brokenPhones = brokenPhones