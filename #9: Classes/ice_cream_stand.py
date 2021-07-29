from restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.favors =[]

    def display_favors(self):
        print("\nWe have following favors:")
        for favor in self.favors:
            print(f"- {favor.title()}")
