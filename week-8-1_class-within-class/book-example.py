from .Author import Author
from .Book import Book, Test
# this is a way to impor multiple classes
# or from .Book import Book, * it will import everything in the file (Classes part 2 - slide 19)

a1 = Author("Bob", "BobNick")
b1 = Book("Shining", a1)