motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles, "\n")

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles, "\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
del motorcycles[1]
print(motorcycles, "\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)
too_expencive = 'ducati'
motorcycles.remove(too_expencive)
print(motorcycles)
print(f"A {too_expencive.title()} is too expencive for me.\n")

# 3.4.
names = ['Anna', 'Jane', 'John']
print(f"Hello, {names[0]}! I want to invite you to a party!")
print(f"Hello, {names[1]}! I want to invite you to a party!")
print(f"Hello, {names[2]}! I want to invite you to a party!\n")

# 3.5.
del_name = names.pop(1)
print(del_name)
names.insert(1, 'Kate')
print(f"Hello, {names[0]}! I want to invite you to a party!")
print(f"Hello, {names[1]}! I want to invite you to a party!")
print(f"Hello, {names[2]}! I want to invite you to a party!\n")

# 3.6.
print("I found a bigger table, so I can invite more people.")
names.insert(0, 'Mike')
names.insert(2, 'Sofi')
names.append('Zak')
print(f"Hello, {names[0]}! I want to invite you to a party!")
print(f"Hello, {names[1]}! I want to invite you to a party!")
print(f"Hello, {names[2]}! I want to invite you to a party!")
print(f"Hello, {names[3]}! I want to invite you to a party!")
print(f"Hello, {names[4]}! I want to invite you to a party!")
print(f"Hello, {names[5]}! I want to invite you to a party!\n")

# 3.7.
print("Planes changed, I can invite onyl two people.")
del_name = names.pop()
print(f"Hello, {del_name}!. I'm sorry, it looks I can't invite ypu to a party.")
del_name = names.pop()
print(f"Hello, {del_name}!. I'm sorry, it looks I can't invite ypu to a party.")
del_name = names.pop()
print(f"Hello, {del_name}!. I'm sorry, it looks I can't invite ypu to a party.")
del_name = names.pop()
print(f"Hello, {del_name}!. I'm sorry, it looks I can't invite ypu to a party.")
print(f"Hello, {names[0]}! I want to invite you to a party!")
print(f"Hello, {names[1]}! I want to invite you to a party!\n")
del names[1]
del names[0]
print(names)
