class Car:
    """Проста спроба змоделювати машину."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


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

    # 9.9.
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


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
