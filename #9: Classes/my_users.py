from users import User


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
