class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.name.title()}.")
        print(f"Cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.name.title()} is open now.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
