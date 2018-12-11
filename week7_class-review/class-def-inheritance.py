

# animal inheritance basic structure add define
class Animal():
        name = ""

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

d = Dog()
d.name = "spot"
c = Cat()
c.name = "Felix"

d.make_sound()
c.make_sound()