# Почати з користувачів, яких треба перевірити,
#  та порожнього списку підтвердження користувачів.
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# Перевіряти кожного користувача, доки непідтверджені користувачі не
# закінчаться.
# Переносити кожного перевіреного користувача до списку підтвердження
# користувачів.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Показати всіх підтверджених користувачів.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
