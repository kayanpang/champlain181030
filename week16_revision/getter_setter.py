class Item():
    def __init__(self, description: str, price: float):
        self.__description = description
        self.__price = price

    def get_description(self):
        # no value in () is needed (self, description) this is to get a value so no need to assign a value to it
        return self.__description
    def set_description(self, new_description: str):
        # now a value in () is needed because it's providing a value
        self.__description = new_description