# chapter9_car
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


my_car = Car('audi', 'a4', 2016)
my_car.get_descriptive_name()
my_car.read_odometer()
my_car.update_odometer(23)
my_car.read_odometer()
my_car.increment_odometer(5)
my_car.read_odometer()