"""this modules contains the classes that defines users"""
class User:
    """this is the class of website user"""
    def __init__ (self, first_name, last_name, location, age, login_attempt):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.age=age
        self.login_attempt=login_attempt

    def describe_user(self):
        """this module summarize the info we have on each user"""
        print("user informations:")
        print(f"\tFirst name: {self.first_name}")
        print(f"\tLast name: {self.last_name}")
        print(f"\tLocation: {self.location}")
        print(f"\tAge: {self.age}")
    def greet_user(self):
        """this module print a customized greeting"""
        print(f"Hello {self.first_name}, welcome back!")

    def increment_login_attempts(self):
        """increments value login by 1"""
        self.login_attempt+=1

    def reset_login_attempts(self):
        """resets the value of login attempts to 0"""
        self.login_attempt=0

    def print_login_attempts (self):
        """prints how many login attempted"""
        print (f"user logged in {self.login_attempt} times")

