class Book:
    def __init__(self, name, author):
        self.page = 0
        self.name = name
        self.author = author

class Author:
    def __init__(self, name, pen):
        self.name = name
        self.pen_name = pen
    def sing(self):
        print("Singing")

a1 = Author("Steven King", True)
b1 = Book("Thinner", a1)
b1.author.sing()