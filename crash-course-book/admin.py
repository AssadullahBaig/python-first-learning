from use import User

class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges([])
   
class Privileges():

    def __init__(self, privileges):
        self.privilege = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("- " + privilege)