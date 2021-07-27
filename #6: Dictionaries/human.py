# 6.1.
human_0 = {
    'first_name': 'john',
    'last_name': 'connor',
    'age': 44,
    'city': 'los angeles',
}

print(human_0)
print(human_0['first_name'].title())
print(human_0['last_name'].title())
print(human_0['age'])
print(human_0['city'].title())


# 6.7.
human_1 = {
    'first_name': 'sofi',
    'last_name': 'monet',
    'age': 25,
    'city': 'paris',
}

human_2 = {
    'first_name': 'daichi',
    'last_name': 'arai',
    'age': 31,
    'city': 'tokio',
}

people = [human_0, human_1, human_2]

for human in people:
    name = f"{human['first_name'].title()} {human['last_name'].title()}"
    age = human['age']
    city = human['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")
