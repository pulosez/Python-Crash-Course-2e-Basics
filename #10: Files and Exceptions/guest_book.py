# 10.4.
file_name = 'text_files/guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("What is your name? ")
    if name == 'quit':
        break
    else:
        print(f"Hello, {name}!")
        with open(file_name, 'a') as file_object:
            file_object.write(f"{name.title()}\n")
