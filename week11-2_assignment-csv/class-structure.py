import datetime
class Document:
    def __init__(self, date, author = []):
        # the parameter can be made as array?
        self.__author = author
        self.__date = datetime.datetime.now()
    def getAuthor(self):
        return self.__author

    def addAuthor(self, name):
        self.__author.append(name)

    def getDate(self):
        return self.__date

class Email(Document):
    def __init__(self, subject, to = []):
        self.__subject = subject
        self.__to = to

    def getSubject(self):
        return self.__subject
    def getTo(self):
        return self.__to

class Book(Document):
    def __init__(self, title = ""):
        self.__title = title

    def getTitle(self):
        return self.__title
