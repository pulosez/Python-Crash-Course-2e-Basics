requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!\n")


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?\n")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                        'pinapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry we don't have {requested_topping}.")
print("Finished making your pizza!\n")
