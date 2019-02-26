# encapsulation
class Person:
    name = ""
    __age = 0

    def setAge(self, a):
        self.__age = a


p = Person()

p.setAge(22)