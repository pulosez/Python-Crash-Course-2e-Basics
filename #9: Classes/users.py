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
