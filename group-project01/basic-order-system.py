import datetime
class Item:
    dot_line = '.' * 30
    def __init__(self, name, price, taxable):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

    def print_item(self):
        print("self.name" + "len(dot_line) - len(self.name) - len(self.price)" + "self.price" + "self.taxable")

    def get_item_base_price(self):
        return self.price

    def get_item_tax_price(self):
        if (self.taxable == True):
            return True
        else:
            return False

    def get_tax(self):
        if (self.taxable == True):
            return self.price*0.05 + self.price*0.09975


    def get_item_total(self):
        return self.get_item_base_price + self.get_tax

class Order:
    x = datetime.datetime.now("%Y-%m-%d %I:%M%p")
    def __init__(self, items, purchase_date):
        self.items = []
        self.purchase_date = x

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(item):
        self.items.remove(item)

    def get_total_price(self):
        return sum(self.price: float)

    def print_summary(self):
        width = " "*50
        width2 = " "*10
        header = "ITEM" + width + "PRICE" + width2 + "TAXABLE"
        line = "-"*len(header)


