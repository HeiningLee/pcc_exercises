# class IceCreamStand
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


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['chocolate', 'cheese', 'vanilla']

    def show_flavors(self):
        print(self.name.title() + " provides the following flavors:")
        for flavor in self.flavors:
            print(flavor)


miki = IceCreamStand('miki', 'icecreams')
miki.show_flavors()
