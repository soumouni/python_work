#try it yourself page 162
#9-1 restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """initializing restaurant's attribute"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        """modules that prints a description of the restaurant"""
        print(f"The {self.restaurant_name} is a place where you can eat" 
            f" {self.cuisine_type} type of food\n")

    def open_restaurant(self):
        """indicates that restaurant is open"""
        print(f"{self.restaurant_name} is now open\n")
    
    def print_number(self):
        """prints the number of customer served"""
        print(f" this restaurant has served {self.number_served}")

    def set_number_served(self, number):
        """updates the number of customer with new value"""
        self.number_served=number
    
    def increment_number_served (self, incr):
        """increment the number of customer served"""
        self.number_served+=incr

restaurant=Restaurant('taj mahal', 'indian food')
print(f"restaurant name is {restaurant.restaurant_name}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.print_number()
restaurant.set_number_served(15)
restaurant.print_number()
restaurant.increment_number_served(20)
restaurant.print_number()

#9-2 Three restaurant
restaurant_2=Restaurant('QG', 'american')
restaurant_3=Restaurant('Rosso pomodoro', 'italian')
restaurant_4=Restaurant('Djazair', 'traditional')
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
restaurant_4.describe_restaurant()

#9-3 Users
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

user_1=User('souad', 'mimouni', 'algiers', 37,0)
user_2=User('walid', 'mimouni', 'montreal',31,0)

user_1.greet_user()
user_1.describe_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
user_1.print_login_attempts()
print()
user_2.greet_user()
user_2.describe_user()
user_2.increment_login_attempts()
user_2.reset_login_attempts()
user_2.print_login_attempts()