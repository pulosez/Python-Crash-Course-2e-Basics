def make_pizza(size, *toppings):
    """Описати піцу, яку ми збираємося приготувати"""
    print(f"\nMaking a {size}-inch pizza with the followig toppings:")
    for topping in toppings:
        print(f"- {topping}")
