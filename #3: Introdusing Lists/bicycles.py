bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles, "\n")

print(bicycles[0])
print(bicycles[0].title(), "\n")

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1], "\n")

message = f"My first bicycle was a {bicycles[0].title()}."
print(message, "\n")

# 3.1.
names = ["katya", "masha", "nastya"]
print(names[0])
print(names[1])
print(names[2])

# 3.2.
message = f"Hello, {names[0].title()}! Nice to meet you!"
print(message)
message = f"Hello, {names[1].title()}! Nice to meet you!"
print(message)
message = f"Hello, {names[2].title()}! Nice to meet you!"
print(message, "\n")

# 3.3.
books = ["Lord of the Rings", "Harry Potter","The First Law"]
message = f"{books[0]} is the basis of fantasy."
print(message)
message = f"{books[1]} is very popular with teenagers."
print(message)
message = f"{books[2]} is very impressive."
print(message)
