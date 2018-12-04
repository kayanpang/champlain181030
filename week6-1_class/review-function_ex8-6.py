# python 8.6 to return
def city_country(city, country):
    return city + ", " + country

print(city_country("Montreal", "Canada"))

# suugestion beginner
def city_country(city, country):
    # return str(city) + ", " + str(country)
    return "{0}, {1}".format(city, country)
