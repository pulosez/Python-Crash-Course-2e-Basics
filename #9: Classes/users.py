# 9.(3, 5).
class User:

    def __init__(self, first_name, last_name, username, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_0 = User('john', 'frost', 'jfrost', 'johnfrost@mail.com', 27)
user_0.describe_user()
user_0.greet_user()

user_1 = User('may', 'tanaka', 'mtanaka', 'maytanaka@mail.com', 25)
user_1.describe_user()
user_1.greet_user()

for value in range(1, 4):
    user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)
