# 7.4.
prompt = "\nPlease enter the topping you want:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
