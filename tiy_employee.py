# Try it yourself page 221
#11-3 Employee
class Employee:
    """this class keeps info about employee"""
    def __init__ (self, first_name, last_name, salary):
        """stores basic infor about employee"""
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary

    def give_raise(self, amout=5000):
        """gives salary raise"""
        self.salary = self.salary + amout

