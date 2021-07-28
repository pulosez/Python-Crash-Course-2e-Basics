def build_profile(first, last, **user_info):
    """Створити словник, що міститиме всю інформацію про користувача."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)


# 8.13.
user_profile = build_profile('sofia', 'moroz',
                            location='lviv',
                            hobby='painting',
                            age=22)
print(user_profile)
