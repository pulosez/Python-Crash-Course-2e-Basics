# 10.12.
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Tell me your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(f"I know your favorite number! It's {number}.")
