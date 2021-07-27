cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")

# 5.1.
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi', "\n")

food = 'pizza'
print("Is food == 'pizza'? I predict True.")
print(food == 'pizza')
print("Is food == 'ice cream'? I predict False.")
print(food == 'ice cream', "\n")

name = 'john'
print("Is name == 'john'? I predict True.")
print(name == 'john')
print("Is name == 'jane'? I predict False.")
print(name == 'jane', "\n")

number = 5
print("Is number == '5'? I predict True.")
print(number == 5)
print("Is number == '7'? I predict False.")
print(number == 7, "\n")

topping = 'pepperoni'
print("Is topping == 'pepperoni'? I predict True.")
print(topping == 'pepperoni')
print("Is topping == 'mushrooms'? I predict False.")
print(topping == 'mushrooms', "\n")

# 5.2.
string = 'Test'
print("Is string == 'test'? I predict True.")
print(string.lower() == 'test')
print("Is string == 'test'? I predict False.")
print(string == 'test', "\n")

age = 18
print("Age > 18? False")
print(age > 18)
print("Age < 21? True")
print(age < 21)
print("Age >= 18? True")
print(age >= 18)
print("Age <= 16? False")
print(age <= 16, "\n")

age_0 = 16
age_1 = 21
print("Age 0 > 18 and Age 1 > 18? False")
print(age_0 > 18 and age_1 > 18)
print("Age 0 > 18 or Age 1 > 18? True")
print(age_0 > 18 or age_1 > 18, "\n")

books = ['harry potter', 'lord of the rings', 'the first law']
book = 'the green mile'
print("'the green mile' is in the list of books? False")
print(book in books)
books.append(book)
print("'the green mile' is in the list of books? True")
print(book in books)
