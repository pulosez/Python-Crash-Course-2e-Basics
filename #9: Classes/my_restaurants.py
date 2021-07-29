from restaurant import Restaurant as R
from ice_cream_stand import IceCreamStand as ICS


restaurant_0 = R('k food', 'korean food')
restaurant_0.describe_restaurant()

restaurant_1 = R('i love kebab', 'kebab')
restaurant_1.describe_restaurant()

restaurant_2 = R('mc donald\'s', 'burger')
restaurant_2.describe_restaurant()

print(restaurant_2.number_served)
restaurant_2.number_served = 420
print(restaurant_2.number_served)

restaurant_2.set_number_served(560)
print(restaurant_2.number_served)

restaurant_2.increment_number_served(470)
print(restaurant_2.number_served)

ice_cream_stand_0 = ICS('limo')
ice_cream_stand_0.favors = ['chocolate', 'vanilla', 'mango', 'banana']
ice_cream_stand_0.describe_restaurant()
ice_cream_stand_0.display_favors()
