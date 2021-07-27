def greet_users(names):
    """"Вивести просте повідомлення для кожного користувача у списку."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hanah', 'ty', 'margot']
greet_users(usernames)
