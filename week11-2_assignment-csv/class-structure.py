class Document:
    def __init__(self, author=[], date):
        self.__author = author
        self.__date = datetime.datetime.now()
    def getAuthor(self):

class Email(Document):
    def __init__(self, subject, to=[]):
        self.__subject = subject
        self.__to = to

class Book(Document):
