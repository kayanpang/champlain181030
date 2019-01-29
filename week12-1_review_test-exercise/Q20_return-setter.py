class Book:
    def __init__(self, name, author):
        self.__name = name
        self.__author = author

    # name and author are set as private so need to use getter setter
    # google should setter return a value
    def get_name(self):
        # get imply you need something in return, so use return
        return self.__name

    def get_author(self):
        return self.__author

    def set_name(self, name):
        self.__name = name
        # should we return self.__name

    def set_author(self, author):
        self.__author = author

my_book1 = Book(None, None)
my_book1.set_name("Book Name Here")

print("My book's name is " + my_book1.get_name())