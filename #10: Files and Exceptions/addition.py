# 10.6.
print("Give me two numbers, and I'll add them.")

first_number = input("\nFirst number: ")
second_number = input("\nSecond number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please enter numbers, not something else!")
else:
    print(answer)
