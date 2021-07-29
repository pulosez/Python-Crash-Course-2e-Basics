# 9.13.
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die6 = Die()
attempts = []
for attempt in range(1, 11):
    attempts.append(die6.roll_die())
print(f"\nAll attempts for {die6.sides}-sided die:")
print(attempts)

die10 = Die(10)
attempts = []
for attempt in range(1, 11):
    attempts.append(die10.roll_die())
print(f"\nAll attempts for {die10.sides}-sided die:")
print(attempts)

die20 = Die(20)
attempts = []
for attempt in range(1, 11):
    attempts.append(die20.roll_die())
print(f"\nAll attempts for {die20.sides}-sided die:")
print(attempts)
