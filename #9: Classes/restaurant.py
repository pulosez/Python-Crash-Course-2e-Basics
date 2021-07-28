# 9.(1, 2, 4).
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


restaurant_0 = Restaurant('k food', 'korean food')
restaurant_0.describe_restaurant()

restaurant_1 = Restaurant('i love kebab', 'kebab')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('mc donald\'s', 'burger')
restaurant_2.describe_restaurant()

print(restaurant_2.number_served)
restaurant_2.number_served = 420
print(restaurant_2.number_served)

restaurant_2.set_number_served(560)
print(restaurant_2.number_served)

restaurant_2.increment_number_served(470)
print(restaurant_2.number_served)
