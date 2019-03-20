class User:
    def __init__(self, f_name, l_name, year_of_birth, city):
        self.f_name = f_name
        self.l_name = l_name
        self.year_of_birth = year_of_birth
        self.city = city
        self.full_name = f_name + ' ' +l_name
        self.login_attempts = 0

    def describe_user(self):
        print("\n--- " + self.full_name.title() + " ---")
        print("YOB:  " + str(self.year_of_birth))
        print("City: " + self.city.title())
        print("Login Attempts:" + str(self.login_attempts))

    def greet_user(self):
        print("\nHello, " + self.full_name.title() + "!")

    def read_attempts(self):
        print(self.full_name.title() + "'s attempts: "
              + str(self.login_attempts))

    def reset_attempts(self):
        self.login_attempts = 0
        print("\nThe number of login attempts is resetted.")

    def increment_attempts(self):
        self.login_attempts = self.login_attempts + 1


class Admin(User):
    def __init__(self, f_name, l_name, year_of_birth, city):
        super().__init__(f_name, l_name, year_of_birth, city)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.full_name.title() + " have the following privileges:")
        for privilege in self.privileges:
            print(privilege)

admin1 = Admin('li', 'zejun', 1995, 'zhu hai')
admin1.show_privileges()