# Add served number to the restaurant class
class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.num_served = 0

    def describe(self):
        print(self.name.title() + " provides " + self.type + ".")

    def open(self):
        print(self.name.title() + " is openning.")

    def read_served(self):
        print(self.name.title() + " has served " +
              str(self.num_served) + " people.")

    def update_served(self, number):
        if number >= self.num_served:
            self.num_served = number
        else:
            print("The number of served people don't decrease.")
        print("The number of served people updated.")

    def increment_served(self, increment):
        if increment >= 0:
            self.num_served = self.num_served + increment
        else:
            print("The number of served people don't decrease.")
        print("The number of served people updated.")


xibi = Restaurant('xibi', 'seafood')
xibi.describe()
xibi.open()
xibi.read_served()
xibi.update_served(200)
xibi.read_served()
xibi.increment_served(300)
xibi.read_served()
