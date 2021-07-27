# 5.8-9.
users = ['jane', 'john', 'admin', 'anna', 'michael']
#users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for loggin in again.")
else:
    print("We need to find some users!")
