class Item:
    # tell what is the last number used
    last_serial_used = 0
    def __init__(self, name, price, taxable):
        self.item_number = Item.last_serial_used + 1
        self.name = name
        self.price = price
        self.taxable = taxable
        Item.last_serial_used = self.item_number
    @staticmethod
    def print_last_serial_used():
        print(Item.last_sku_used)

a1 = Item("first item", 2.00, True)
a2 = Item("Second Item", 3.00, False)

print(a1.item_number)
print(a2.item_number)