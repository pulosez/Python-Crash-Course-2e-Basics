# 10.5.
file_name = 'text_files/programming_poll.txt'

print("Enter 'quit' when you are finished.")
while True:
    answer = input("Why do you love programming? ")
    if answer == 'quit':
        break
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(f"{answer}\n")
