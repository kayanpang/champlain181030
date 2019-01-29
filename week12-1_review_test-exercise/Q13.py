class Author:
    def __init__(self, name, pen):
        self.name = name
        self.pen = pen

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

a1 = Author("Steven King", True)
book1 = Book("Test Book", a1)

print("The author of the book is " + book1.author.name)