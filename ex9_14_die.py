''' This is a die simulation program. Interpreting the module "random"'''

from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, rolltimes):
        print("Rolling the " + str(self.sides) + " sides dice for "
              + str(rolltimes) + " times...")
        for rolltime in range(1, rolltimes+1):
            print(str(randint(1, self.sides)))


die1 = Die(6)
die1.roll_die(10)

die2 = Die(20)
die2.roll_die(10)
