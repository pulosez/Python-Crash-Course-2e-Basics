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


# 9.(7, 8).
class Admin(User):

    def __init__(self, first_name, last_name, username, email, age):
        super().__init__(first_name, last_name, username, email, age)
        self.privileges = []

    def show_privileges(self):
        print("\nThis admin has such privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


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

admin_0 = Admin('anna', 'smith', 'asmith', 'annasmith@mail.com', 29)
admin_0.privileges = ['can add post', 'can delete post', 'can ban user']
admin_0.describe_user()
admin_0.show_privileges()
