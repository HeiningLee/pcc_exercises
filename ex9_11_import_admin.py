'''Before class Admin's definition, it's super class User
 is imported in the module mod_admin.'''

from mod_admin import Admin
user1 = Admin('li', 'zejun', 1995, 'zhu hai')
user1.show_privileges()
