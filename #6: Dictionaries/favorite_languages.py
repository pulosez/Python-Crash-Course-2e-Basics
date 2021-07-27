favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print ("Erin, please take our poll!")


print("\n")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for talking the poll.")


print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

print("\n")
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


# 6.6.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

names = ['jen', 'sarah', 'edward', 'phil', 'ann', 'john', 'jane']

print("\n")
for name in names:
    if name in favorite_languages.keys():
        print(f"Thankk you, {name.title()}!")
    else:
        print(f"{name.title()}, what is your favorite language?")
