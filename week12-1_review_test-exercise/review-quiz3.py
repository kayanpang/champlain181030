# in python one class cannot have more than 1 __init__
class Q3:
    def __init__(self):
        print("do something")
    def __init__(self, name):
        print("Hello " + name)

q = Q3
q1 = Q3("Brendon")