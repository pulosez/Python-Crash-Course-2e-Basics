my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoil')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods, "\n")

# 4.11.
pizzas = ['pepperoni', 'cheese', 'margherita']
friend_pizzas = pizzas[:]
pizzas.append('buffalo')
friend_pizzas.append('supreme')
print("My favorite pizzas are:")
print(pizzas)
print("My friend's favorite pizzas are:")
print(friend_pizzas, "\n")

# 4.12.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
