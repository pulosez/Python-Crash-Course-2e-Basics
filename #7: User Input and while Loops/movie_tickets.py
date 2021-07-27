# 7.5.
prompt = "How old are you?"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is $0.")
    elif age < 13:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
