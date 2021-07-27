for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

# 4.3.
for value in range(1, 21):
    print(value)
print("\n")

# 4.4-5.
numbers = list(range(1, 1_000_001))
# for value in numbers:
#     print(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6.
odd_numbers = list(range(1, 20, 2))
for value in odd_numbers:
    print(value)

# 4.7.
three = list(range(3, 31, 3))
for value in three:
    print(value)

# 4.8.
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
for cube in cubes:
    print(cube)

# 4.9.
cubes = [value**3 for value in range(1, 11)]
print(cubes)
