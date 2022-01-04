"""stores class admin and privileges"""
from module_users import User
class Admin(User):
    """defining attributes of admin from parent class 'user' """
    def __init__(self, first_name, last_name, location, age, login_attempt):
        """initializing attributes of admin"""
        super().__init__(first_name, last_name, location, age, login_attempt)
        self.privileges=Privileges()

class Privileges:
    """stores the possible privileges"""
    def __init__(self):
        self.privileges=['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """print the default list of privileges available to admin"""
        print ("bellow is the list of privileges avaiable to admin user")
        for privilege in self.privileges:
            print(privilege)