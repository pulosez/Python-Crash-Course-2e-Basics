# 7.10.
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which place would you like to visit someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
