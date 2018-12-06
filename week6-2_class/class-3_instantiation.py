class Cat:
    name = ""
    age = ""
    registered = False
    # name/age is property
    def __init__(self, input_name, input_age):
        # definition within the class
        self.name = input_name
        self.age = input_age

        if input_age > 2:
            self.registered = True
    def Meow(self, number_times):
        for m in range(number_times):
            print("Meow")
    # OVERLOADING
    def Meow(self, number_times, phrase=""):
        for m in range(number_times):
            print("Meow" + phrase)

# instantiation
c1 = Cat("Jack", 2)
c2 = Cat("Meow", 9)
print("Cat c1 registration state is " + str(c1.registered))
print("Cat c2 registration state is " + str(c2.registered))

c1.Meow(8)