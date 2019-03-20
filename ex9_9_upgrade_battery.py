# ex9_9: Add a function "upgrade battery" to class Battery.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("The odometer can't be rolled back!")
        print("Odometer updated.")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading = self.odometer_reading + miles
        else:
            print("The odometer can't be rolled back!")
        print("Odometer updated.")

    def fill_gas_tank(self):
        print(self.make.title() + "-" + self.model.title()
              + "'s gas tank filled.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        self.battery.describe_battery()
        # print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print(self.make.title() + "-" + self.model.title()
              + " is an electric car. It doesn't have a gas tank!")


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size ==70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


my_audi = Car('audi', 'a4', 2016)
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name().title())
my_tesla.describe_battery()

my_audi.fill_gas_tank()
my_tesla.fill_gas_tank()

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
