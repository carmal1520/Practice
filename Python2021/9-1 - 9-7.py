# # 9-1

# class Restaurant:

#     def __init__(self, r_name, cuisine_type):
#         self.r_name = r_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         name = f"\nName: {self.r_name.title()}"
#         cuisine = f"Cuisine Type: {self.cuisine_type}"
#         print(name)
#         print(cuisine)

#     def open_restaurant(self):
#         message = f"\n{self.r_name.title()} is open. Servering {self.cuisine_type}."
#         print(message)

# restaurant = Restaurant("IHOP", "Breakfast")
# print(restaurant.r_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# # 9-2

# restaurant = Restaurant("Pi Pizzeria", "Pizza")
# print(restaurant.r_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# # 9-3

# class User:

#     def __init__(self, first_name, last_name, username, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.email = email

#     def describe_user(self):
#         user_info = {
#             "First Name": self.first_name,
#             "Last Name": self.last_name,
#             "Username" : self.username,
#             "Email" : self.email,
#         }

#         for x, y in user_info.items():
#             print(f"{x} : {y}")
    
#     def greet_user(self):
#         message = f"Welcome back {self.first_name.title()} {self.last_name.title()}!"
#         print(message)

# user = User("Carlos", "Maldonado", "cmaldo", "cmaldo@live.com")
# user.describe_user()
# user.greet_user()

# user = User("Liam", "arocho", "moose", "larocho@live.com")
# user.describe_user()
# user.greet_user()

#  9-4

# class Restaurant:

#     def __init__(self, r_name, cuisine_type):
#         self.r_name = r_name
#         self.cuisine_type = cuisine_type
#         self.number_served= 0

#     def describe_restaurant(self):
#         name = f"\nName: {self.r_name.title()}"
#         cuisine = f"Cuisine Type: {self.cuisine_type}"
#         print(name)
#         print(cuisine)

#     def open_restaurant(self):
#         message = f"\n{self.r_name.title()} is open. Servering {self.cuisine_type}."
#         print(message)

#     def set_number_served(self, number_served):
#         self.number_served = number_served
    
#     def increment_number_served(self, additional_served):
#         self.number_served += additional_served

# restaurant = Restaurant("IHOP", "Breakfast")
# # print(restaurant.r_name)
# # print(restaurant.cuisine_type)
# # restaurant.describe_restaurant()
# # restaurant.open_restaurant()

# restaurant.set_number_served(5)
# print(restaurant.number_served)
# restaurant.increment_number_served(10)
# print(restaurant.number_served)

# 9-5

# class User:

#     def __init__(self, first_name, last_name, username, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.email = email
#         self.login_attempts = 0

#     def describe_user(self):
#         user_info = {
#             "First Name": self.first_name,
#             "Last Name": self.last_name,
#             "Username" : self.username,
#             "Email" : self.email,
#         }

#         for x, y in user_info.items():
#             print(f"{x} : {y}")
    
#     def greet_user(self):
#         message = f"Welcome back {self.first_name.title()} {self.last_name.title()}!"
#         print(message)
    
#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self. login_attempts = 0

# user = User("Carlos", "Maldonado", "cmaldo", "cmaldo@live.com")
# user.describe_user()
# user.greet_user()

# # user = User("Liam", "arocho", "moose", "larocho@live.com")
# # user.describe_user()
# # user.greet_user()

# print(user.login_attempts)
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attempts)
# user.reset_login_attempts()
# print(user.login_attempts) 

# 9-6

# class Restaurant:

#     def __init__(self, r_name, cuisine_type):
#         self.r_name = r_name
#         self.cuisine_type = cuisine_type
#         self.number_served= 0

#     def describe_restaurant(self):
#         name = f"\nName: {self.r_name.title()}"
#         cuisine = f"Cuisine Type: {self.cuisine_type}"
#         print(name)
#         print(cuisine)

#     def open_restaurant(self):
#         message = f"\n{self.r_name.title()} is open. Servering {self.cuisine_type}."
#         print(message)

#     def set_number_served(self, number_served):
#         self.number_served = number_served
    
#     def increment_number_served(self, additional_served):
#         self.number_served += additional_served


# class IceCreamStand(Restaurant):

#     def __init__(self, r_name, cuisine_type):
#         super().__init__(r_name, cuisine_type)
#         self.flavors = []
    
#     def show_flavors(self):
#         for x in self.flavors:
#             print(x)

# icecream = IceCreamStand("Mr. Softy", "Ice Cream")

# icecream.flavors = ["Stawberry", "Vanilla", "Chocolate"]

# icecream.describe_restaurant()
# icecream.show_flavors()

# 9-7

# class User:

#     def __init__(self, first_name, last_name, username, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.email = email
#         self.login_attempts = 0

#     def describe_user(self):
#         user_info = {
#             "First Name": self.first_name,
#             "Last Name": self.last_name,
#             "Username" : self.username,
#             "Email" : self.email,
#         }

#         for x, y in user_info.items():
#             print(f"{x} : {y}")
    
#     def greet_user(self):
#         message = f"Welcome back {self.first_name.title()} {self.last_name.title()}!"
#         print(message)
    
#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self. login_attempts = 0

# class Amin(User):

#     def __init__(self, first_name, last_name, username, email):
#         super().__init__(first_name, last_name, username, email)
#         self.privileges = Privileges()

# class Privileges():

#     def __init__(self, privileges = []):
#         self.privileges = privileges
        
#     def show_privileges(self):
        
#         if self.privileges:
#             for privilege in self.privileges:
#                 print(privilege)


# carlos = Amin("Carlos","Maldonado", "leeto", "leeto@admin")
# carlos.privileges = ["can add post", "can delete post", "can ban user"]

# liam = Amin('Liam','Arocho', 'Moose', 'moose4life')
# liam.describe_user()

# liam_privileges = ["cant  do anything"]
# liam.privileges.privileges = liam_privileges
# liam.privileges.show_privileges()

# class Car:
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class Battery():
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=75):
#         """Initialize the batteery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
            
#         message = f"This car can go approximately {range}"
#         message += " miles on a full charge."
#         print(message)

#     def upgrade_battery(self):
#         if self.battery_size != 100:
#             self.battery_size = 100
#             print("Battery has been upgraded")
#         else:
#             print("You battery is already upgraded")



# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""

#     def __init__(self, manufacturer, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(manufacturer, model, year)
#         self.battery = Battery()

# car = ElectricCar("Tesla", "Model 3", "2021")
# car.battery.get_range()
# car.battery.upgrade_battery()
# car.battery.get_range()
# print(car.get_descriptive_name())
