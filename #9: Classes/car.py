"""Клас для моделювання автівки."""


class Car:
    """Проста спроба змоделювати машину."""

    def __init__(self, make, model, year):
        """Ініціалізувати атрибути, що описують машину."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Повернути відформатоване змістовне ім'я."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Вивести повідомлення з пробігом машини."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Задати значення одометра.
        Відкинути зміну в разі спроби відмотати показники одометра
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Додати задане значення до показника одометра."""
        self.odometer_reading += miles
