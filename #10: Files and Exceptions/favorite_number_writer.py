import json

filename = 'favorite_number.json'
number = input("Tell me your favorite number: ")

with open(filename, 'w') as f:
    json.dump(number, f)
