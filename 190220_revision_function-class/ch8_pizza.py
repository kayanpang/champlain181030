def make_pizza(size, *toppings):
    # * before topping is to tell python to create a empty tuple and pack whatever values it receives into this tuple
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroons', 'green peppers', 'extra cheese')