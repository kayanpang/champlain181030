# nesting
# a list of dictionaries

# dictionaries
alien_0 = {'color': 'green','points': 5}
alien_1 = {'color': 'red','points': 10}
alien_2 = {'color': 'blue','points': 15}
# making the dictionaries as a list
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# a list in a dictionary
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
print("you ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)

# a dictionary in a dictionary
users = {'aeinstein': {"first": "albert", "last": "einstein", "location": "princeton"},
         'mcurie': {"first": "marie", "last": "curie", "location": "paris"}}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
