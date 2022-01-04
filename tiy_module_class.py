"""this module contains class restaurant"""
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