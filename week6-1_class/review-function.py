# python ex. 8.5 city in a country
def describe_city(city, country = "Unknown country"):
    print(city.title() + " is in " + country.title())
    print("{0} is in {1}".format(city.title, country.title))

describe_city("Montreal", "Canada")
describe_city("Montreal")

