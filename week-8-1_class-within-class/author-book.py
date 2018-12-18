class Author:
    def __init__(self, name, pen):
        self.name = name
        self.pen_name = pen

class Book:
    def __init__(self, name, author: Author):
        self.pages = 0
        self.name = name
        self.author = author

a1 = Author("Bob", "BobNick")
b1 = Book("Shining", a1)