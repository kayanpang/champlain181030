class Animal:
    def make_sound(self):
        print("I make a generic sound")

class Dog(Animal):

    def make_sound(self):
        print("Bark")
    def make_parent_sound(self):
        super().make_sound()

d1 = Dog()
