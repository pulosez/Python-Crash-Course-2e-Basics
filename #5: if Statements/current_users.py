current_users = ['Jane', 'john', 'ann', 'cris', 'mike']
new_users = ['charlie', 'JANE', 'kate', 'zara', 'John']

current_users_copy = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_copy:
        print(f"Sorry, username '{user}' is not available.")
    else:
        print(f"Hello, {user}!")
        current_users.append(user)

print(current_users)
