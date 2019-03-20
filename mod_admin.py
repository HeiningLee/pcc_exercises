from mod_user import User


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Privileges are as follows:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, f_name, l_name, year_of_birth, city):
        super().__init__(f_name, l_name, year_of_birth, city)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()