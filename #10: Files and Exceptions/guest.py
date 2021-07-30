# 10.3.
file_name = 'text_files/guest.txt'

name = input("What is your name? ")
with open(file_name, 'w') as file_object:
    file_object.write(name.title())
