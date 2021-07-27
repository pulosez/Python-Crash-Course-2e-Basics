responses = {}

# Встановиити булеву змінну у значення, що показує: опитування в процесі.
polling_active = True

while polling_active:
    # Спитати ім'я людини та її відповідь.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Зберегти відповідь у словник.
    responses[name] = response

    # Дізнатися, чи збирається хтось іще проходити опитування.
    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False

# Опитування завершене. Показати результати.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
