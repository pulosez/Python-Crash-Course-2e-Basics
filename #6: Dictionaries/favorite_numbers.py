# 6.2.
favorite_numbers = {
    'john': 1,
    'anna': 7,
    'edward': 22,
    'jane': 5,
    'kate': 3,
}

print(favorite_numbers)
num = favorite_numbers['john']
print(f"John's favorite number is {num}.")
num = favorite_numbers['anna']
print(f"Anna's favorite number is {num}.")
num = favorite_numbers['edward']
print(f"Edward's favorite number is {num}.")
num = favorite_numbers['jane']
print(f"Jane's favorite number is {num}.")
num = favorite_numbers['kate']
print(f"Kate's favorite number is {num}.")
print("\n")


# 6.10.
favorite_numbers = {
    'john': [1, 11, 3],
    'anna': [7, 5, 100],
    'edward': [22, 42],
    'jane': [5, 1, 10],
    'kate': [3, 17],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")
    