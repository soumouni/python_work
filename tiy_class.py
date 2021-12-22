#try it yourself page 162
#9-1 restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """initializing restaurant's attribute"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        """modules that prints a description of the restaurant"""
        print(f"The {self.restaurant_name} is a place where you can eat" 
            f" {self.cuisine_type} type of food\n")

    def open_restaurant(self):
        """indicates that restaurant is open"""
        print(f"{self.restaurant_name} is now open\n")


restaurant=Restaurant('taj mahal', 'indian food')
print(f"restaurant name is {restaurant.restaurant_name}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

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
    def __init__ (self, first_name, last_name, location, age):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.age=age
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

user_1=User('souad', 'mimouni', 'algiers', 37)
user_2=User('walid', 'mimouni', 'montreal',31)

user_1.greet_user()
user_1.describe_user()
print()
user_2.greet_user()
user_2.describe_user()