class Animal:
    def __init__(self):
        self.name = ""
# this is what polymorphism is
# 1 tey have the same function name (make_sound)

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def make_sound(self):
        print("Meow")
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def make_sound(self):
        print("Bark")
def invoke_sound_from_object(animal):
    animal.make_sound()