from Items import Item
item1 = Item("myItem",500,2)
item1.apply_increment(0.2)
item1.send_email()
print(item1.price)