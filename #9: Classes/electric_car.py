"""Набір класів, що можуть змоделювати електрокар."""
from car import Car


class Battery:
    """Проста спроба змоделювати акумулятор електрокара."""

    def __init__(self, battery_size=75):
        """Ініціалізувати атрибути акумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Вивести повідомлення про розмір акумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """
        Вивести повідомлення про відстань, яку може подолати авто відповідно до ємності акумулятора.
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"Upgraded battery to {self.battery_size} kWh.")
        else:
            print("This battery doesn't need to be upgraded.")


class ElectricCar(Car):
    """Змоделювати властивості, притаманні електрокарам."""

    def __init__(self, make, model, year):
        """
        Ініціалізувати атрибути бвтьківського класу. Тоді ініціалізувати атрибути електрокара.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
