# 7.3.
number = input("Enter a number, and I'll tell you if it's multiples of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is multiples of ten.")
else:
    print(f"The number {number} is not multiples of ten.")
