# # 2-1
# message = "I like python"
# print(message)

# # 2-2
# message_1 = "I want to learn python"
# print(message_1)
# message_1 = "I really want to learn python"
# print(message_1)

# # 2-3
# name = "Eric"
# print(f"Hello {name.title()}, would you like to learn some Python today?")

# # 2-4
# name = "eric"
# print(name.title())
# print(name.upper())
# print(name.lower())

# # 2-5
# quote = "fear is the mind killer"
# auther = "unknown"
# message = f"{auther.title()} once said '{quote.capitalize()}'"
# print(message)

# # 2-6
# same as 2-5

# # 2-7
# name = "  Liam  "
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())

# # 2-8
# print(2+2)
# print(2-2)
# print(2*2)
# print(2/2)

# # 2-9
# number = 7
# message = f"my favorite number is {number}"
# print(message)

###########

# # 3-1
# names = ["liam", "jordan", "russ", "eric"]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# # 3-2
# names = ["liam", "jordan", "russ", "eric"]
# message = f"My friend is {names[0]}"
# print(message)
# message = f"My friend is {names[1]}"
# print(message)
# message = f"My friend is {names[2]}"
# print(message)
# message = f"My friend is {names[3]}"
# print(message)

# # 3-3
# transportation = ["bike", "car", "train"]
# msg = f"I like to take the {transportation[0]}"
# print(msg)
# msg = f"I like to take the {transportation[1]}"
# print(msg)
# msg = f"I like to take the {transportation[2]}"
# print(msg)

# # 3-4
# dinner_list = []
# dinner_list.append("mom")
# dinner_list.append("liam")
# dinner_list.insert(0, "dad")
# print(f"The dinner list consist of {dinner_list}")
# msg = f"{dinner_list[0]} you are invited to dinner."
# print(msg)
# msg = f"{dinner_list[1]} you are invited to dinner."
# print(msg)
# msg = f"{dinner_list[2]} you are invited to dinner."
# print(msg)

# # 3-5
# dinner_list = []
# dinner_list.append("mom")
# dinner_list.append("liam")
# dinner_list.insert(0, "dad")
# print(f"{dinner_list.pop()} isnt able to make it.")
# dinner_list.insert(3, "jordan")
# print(f"{dinner_list[2]} will be invited instead.")
# print(dinner_list)

# # 3-6
# same as above

# # 3-7
# same as above

# # 3-8
# places = ["japan", "thailand", "korea", "philippines", "tokyo"]
# print(places)
# print(sorted(places))
# print(places)
# print(sorted(places, reverse=True))
# print(places)

# # 3-9
# places = ["japan", "thailand", "korea", "philippines", "tokyo"]
# print(f"I would like to visit {len(places)} places")

# 3-10
# same as above

#########

# # 4-1
# pizzas = ["sasuage", "cheese", "bacon"]
# for pizza in pizzas:
#     print(f" I like {pizza} pizza!")
# print("I really love pizza!")

# # 4-2
# animals = ["dog", "cat", "bird"]
# for animal in animals:
#     print(f"A {animal} would make a great pet")
# print("Any of these animals would make a great pet!")

# # 4-3
# for x in range(1, 21):
#     print(x)

# # 4-4
# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# # 4-6
# numbers = list(range(1, 20, 2))
# for number in numbers:
#     print(number)

# # 4-7
# numbers = list(range(3, 31, 3))
# for number in numbers:
#     print(number)

# # 4-8
# numbers = []
# for x in range(1, 11):
#     number = x ** 3
#     numbers.append(number)
# print(numbers)

# # 4-9
# numbers = [number ** 3 for number in range(1, 11)]
# print(numbers)

# # 4-10
# skip

# # 4-11
# pizzas = ["sasuage", "cheese", "bacon"]
# friend_pizzas = pizzas[:]
# pizzas.append("chicken")
# friend_pizzas.append("turkey")
# for pizza in pizzas:
#     print(f"my favorite pizza is {pizza}")
# for fpizza in friend_pizzas:
#     print(f"\n my favorite pizza is {fpizza}")

# # 4-12
# skip

# # 4-13
# foods = ("chicken", "bread", "turkey", "eggs", "onion rings")
# for food in foods:
#     print(food)
# # foods[0] = "cake" rejected.
# foods = ("chicken", "bread", "turkey", "sausage", "beef")
# for food in foods:
#     print(food)

# # 5-1
# car = 'subaru'
# print("Is car == 'subaru' ? I predict True.")
# print(car == 'subaru')

# food = 'chicken'
# print("Will food == chicken? I think false")
# print(food == 'pizza')

# # 5-2 skip

# # 5-3
# alien_color = "green"
# if alien_color == "green":
#     print("You just earned 5 points")

# alien_color = "blue"
# if alien_color == "green":
#     print("You just earned 5 points")

# alien_color = 'red'
# if alien_color == 'green':
#     print("you just earned 5 points")
# else:
#     print("you just earned 10 points")

# # 5-6
# alien_color = 'red'
# if alien_color == 'green':
#     print("you just earned 5 points")
# elif alien_color == 'yellow':
#     print("you just earned 10 points")
# elif alien_color == 'red':
#     print("you just earned 15 points")

# # 5-6
# age = 65
# if age < 2:
#     print("you are a baby")
# elif age < 4:
#     print("you are a toddler")
# elif age < 13:
#     print("you are a kid")
# elif age < 20:
#     print("you are a teenager")
# elif age < 65:
#     print("you are an adult")
# else:
#     print("you are an elder")

# # 5-7
# favorite_fruits = ['strawberry', 'orange', 'apple']
# if 'strawberry' in favorite_fruits:
#     print("you really like strawberries")
# if 'orange' in favorite_fruits:
#     print("you really like oranges")
# if 'apple' in favorite_fruits:
#     print("you really like apples")
# if 'pear' in favorite_fruits:
#     print('you really like pears')
# else:
#     print("you dont like that")

# # 5-8
# usernames = ['admin', 'leeto', 'moose', 'kekw', 'toto']
# if usernames:
#     for name in usernames:
#         if name == 'admin':
#             print(f"Hello {name}, welcome back")
#         else:
#             print(f"Hello {name}, welcome to the danger zone")
# else:
#     print("we need to find more users")

# # 5-9
# same as above

# # 5-10
# current_users = ['moose', 'jshadow', 'shadowstep', 'surshado', 'leeto']
# new_users = ['moose', 'JSHADOW', 'roota', 'longpillow', 'leftshark']

# for user in new_users:
#     if user.lower() in current_users:
#         print(f"{user.title()} is not available.")
#     else:
#         print(f"{user} is available.")

# # 5-11
# numbers = list(range(1, 10))
# for number in numbers:
#     if number == 1:
#         print(f"{number}st")
#     elif number == 2:
#         print(f"{number}nd")
#     elif number == 3:
#         print(f"{number}rd")
#     else:
#         print(f"{number}th")

# # 6-1
# liam = {
#     "First Name" : "Liam",
#     "Last Name" : "Arocho",
#     "Age" : 34,
#     "City" : "Chesapeake"
# }

# for key, value in liam.items():
#     print(key, value)

# # 6-2
# favorite_numbers = {
#     "liam" : 34,
#     "jordan" : 11,
#     "russell" : 26,
#     "eric" : 88,
#     "leeto" : 14
# }

# for key, value in favorite_numbers.items():
#     print(f" {key.title()}'s favorite number is {value}")

# # 6-3 - 6-4 - 6-5 - 6-6
# skip

# # 6-7
# liam = {
#     "First Name" : "Liam",
#     "Last Name" : "Arocho",
#     "Age" : 34,
#     "City" : "Chesapeake"
# }

# eric = {
#     "First Name" : "Eric",
#     "Last Name" : "Broadnax",
#     "Age" : 34,
#     "City" : "Chesapeake"
# }

# russell = {
#     "First Name" : "Russell",
#     "Last Name" : "Wesh",
#     "Age" : 34,
#     "City" : "Chesapeake"
# }

# people = [liam, eric, russell]

# for friend in people:
#     for key, value in friend.items():
#         print(f"{key}, {value}")

# # 6-8
# pets = []

# animal = {
#     "Animal Type" : "Dog",
#     "Animal Name" : "fuji",
#     "Age" : 1,
#     "City" : "Virginia Beach"
# }
# pets.append(animal)
# animal = {
#     "Animal Type" : "Cat",
#     "Animal Name" : "fro",
#     "Age" : 3,
#     "City" : "Chesapeake"
# }
# pets.append(animal)
# animal = {
#     "Animal Type" : "Bird",
#     "Animal Name" : "pebble",
#     "Age" : 10,
#     "City" : "Suffolk"
# }
# pets.append(animal)

# if pets:
#     for pet in pets:
#         for key, value in pet.items():
#             print(f"{key} {value}")

# # 6-9
# favorite_places = {
#     "leeto" : ["Japan", "Tokyo", "Fussa"],
#     "Liam" : "Chesapeake",
#     "Eric" : "Norfolk"
# }
# for key, value in favorite_places.items():
#     print(f"My friend {key.title()}'s favorite place is {value}")

# # 6-10
# favorite_numbers = {
#     "liam" : [34, 11, 15, 18],
#     "jordan" : [11, 12, 13 ,14],
#     "russell" : [26, 27 ,28, 29],
#     "eric" : [88, 89, 90],
#     "leeto" : [14]
# }

# for name, numbers in favorite_numbers.items():
#     print(f"\nHello {name.title()}, here are your favorite numbers:")
#     for number in numbers:
#         print(f" \t-{number}")

# # 6-11 - 6-12
# skip

# # 7-1
# prompt = input("What kind of rental car would you like? ")
# print(f"let me see if i can find a {prompt} for you")

# # 7-2
# group = int(input("How many people are in your dinner group? "))
# if group > 8:
#     print("You will have to wait for a table.")
# else:
#     print("Your table is ready.")

# # 7-3
# number = int(input("Please input a number: "))
# if number % 10 == 0:
#     print(f"{number} is a multiple of 10")
# else:
#     print(f"{number} is not a multiple of 10")

# # 7-4
# prompt = "Please enter a pizza topping"
# prompt += "\n\tEnter 'quit' to exit: "
# while True:
#     topping = input(prompt)
#     if topping.lower() != 'quit':
#         print(f"{topping} will be added to the pizza.")
#     else:
#         break

# # 7-5
# age = int(input("Enter your age: "))
# active = True
# while active:
#     if age < 3:
#         print("Your ticket is free")
#         break
#     elif age <= 12:
#         print("Your ticket is $10")
#         break
#     else:
#         print("Your ticket is $15")
#         break

# # 7-6 7-7 skip

# # 7-8
# sandwich_orders = ["Turkey", "BLT", "Salami"]
# finished_sandwiches = []

# while sandwich_orders:
#     for x in sandwich_orders:
#         print(f"{x} sandwhich is being prepared")
#         finished_sandwiches.append(x)
#     print(f"The following sandwhiches were made {finished_sandwiches}")
#     break

# # 7-9
# sandwhich_orders = ["Turkey", "pastrami", "BLT", "pastrami", "Salami", "pastrami"]
# finished_orders = []

# print("The deli is out of pastrami")
# while "pastrami" in sandwhich_orders:
#     sandwhich_orders.remove("pastrami")

# while sandwhich_orders:
#     for current_order in sandwhich_orders:
#         current_order = sandwhich_orders.pop()
#         print(f"{current_order.title()} Sandwich is being made.")
#         finished_orders.append(current_order)

# for complete_order in finished_orders:
#     print(f"The following sandwhichs are finished: {complete_order}")
# print(finished_orders)

# # 7-10
# responses = {}

# polling_active = True

# while polling_active:
#     name = input("What is your name? ")
#     response = input("Which city would you like to visit? ")

#     responses[name] = response

#     repeat = input("Would you like to let another person respond?  (yes/no) ")
#     if repeat == 'no':
#         polling_active = False

# print("--Poll Results--")
# for name, response in responses.items():
#     print(f"{name} would like to visit {response}")

# # 8-1
# def display_message():
#     print("I am reviewing all chapters")

# display_message()

# # 8-2
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")

# favorite_book("Python Crash Course")

# # 8-3
# def make_shirt(shirt_size, shirt_text):
#     print(f"Your shirt size is {shirt_size} and the message is {shirt_text}")

# make_shirt("large", "I love python")
# make_shirt(shirt_size="small", shirt_text="I dont like python")

# # 8-4
# def make_shirt(shirt_text, shirt_size="large"):
#     print(f"Shirt Size: {shirt_size}")
#     print(f"Shirt Message: {shirt_text}")

# make_shirt("I love Python")
# make_shirt("I love food", shirt_size="medium")

# # 8-5
# def describe_city(name, country="Japan"):
#     print(f"{name} is located in {country}")

# describe_city("Tokyo")
# describe_city("New York", country='USA')
# describe_city("Fussa")

# # 8-6
# def city_country(city_name, country):
#     full_location = f"{country} : {city_name}"
#     return full_location.title()

# location = city_country("Tokyo", "Japan")
# print(location) 

# # 8-7
# def make_album(artist_name, album_title):
#     x = {
#         "Artist Name" : artist_name,
#         "Album Title" : album_title
#     }
#     return x
# musician = make_album("Magic Dragons", "Arcane")
# print(musician)

# # 8-8
# def make_album(artist_name, album_title):
#     x = {
#         "Artist Name" : artist_name,
#         "Album Title" : album_title
#     }
#     return x

# print("\nPlease enter an artist name:")
# print("enter 'q' to quit at anytime")

# while True:
#     aname = input("Artist Name: ")
#     if aname == 'q':
#         break
#     atitle = input("Album Title: ")
#     if atitle == 'q':
#         break
#     music = make_album(aname, atitle)
#     print(music)

# # 8-9
# def show_messages(messages):
#     for x in messages:
#         print(x)

# messages = ["I Like Python", "We eat chicken", "I like Amazon"]
# show_messages(messages)

# # 8-10
# unsent_messages = ["I Like Python", "We eat chicken", "I like Amazon"]
# sent_messages = []

# def send_messages(unsent_messages, sent_messages):
#     while unsent_messages:
#         current_message = unsent_messages.pop()
#         sent_messages.append(current_message)
#     print(sent_messages)

# def show_messages(messages):
#     for x in messages:
#         print(x)

# show_messages(unsent_messages)
# send_messages(unsent_messages, sent_messages)
# print(unsent_messages)
# print(sent_messages)

# # 8-11
# unsent_messages = ["I Like Python", "We eat chicken", "I like Amazon"]
# sent_messages = []

# def send_messages(unsent_messages, sent_messages):
#     while unsent_messages:
#         current_message = unsent_messages.pop()
#         sent_messages.append(current_message)
#     print(sent_messages)

# def show_messages(messages):
#     for x in messages:
#         print(x)

# send_messages(unsent_messages[:], sent_messages)
# print(unsent_messages)

# # 8-12
# def sandwiches(*items):
#     print(items)

# sandwiches("salami")
# sandwiches("lettuce", "cheese", "ham")

# # 8-13
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein',
#                             location='princeton',
#                             field='physics')
# print(user_profile)

# user_profile = build_profile("Carlos", "Maldonado", location="Arlington", field="Computer Science")
# print(user_profile)

# # 8-14
# def make_car(manufacturer, model_name, **car_info):
#     car_dict = {
#         'manufacturer' : manufacturer.title(),
#         'model' : model_name.title(),
#         }

#     for x, y in car_info.items():
#         car_dict[x] = y

#     return car_dict

# my_car = make_car("Mazda","Mazda 3", year=2015)
# print(my_car)

# def make_car(manufacturer, model, **options):
#     """Make a dictionary representing a car."""
#     car_dict = {
#         'manufacturer': manufacturer.title(),
#         'model': model.title(),
#         }
#     for option, value in options.items():
#         car_dict[option] = value

#     return car_dict

# my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(my_outback)

# # 8-15
# import printing_example as pe

# unprinted_designs = ['iphone case', 'robot', 'dog statue']
# completed_models = []

# pe.print_models(unprinted_designs, completed_models)
# pe.show_completed_models(completed_models)

# # 9-1
# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type

#     def describe_resturant(self):
#         rest_name = f"{self.name}"
#         food_type = f"{self.cuisine_type}"
#         statement = f"Welcome to {rest_name.title()}, we sell {food_type} food."
#         return statement

#     def open_restaurant(self):
#         msg = f"{self.name} is open"
#         return msg

# restaurant = Restaurant("Wendys", "Fast Food")
# print(restaurant.describe_resturant())
# print(restaurant.open_restaurant())
# print(restaurant.name)
# print(restaurant.cuisine_type)

# # 9-2
# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type

#     def describe_resturant(self):
#         rest_name = f"{self.name}"
#         food_type = f"{self.cuisine_type}"
#         statement = f"Welcome to {rest_name.title()}, we sell {food_type}."
#         return statement

#     def open_restaurant(self):
#         msg = f"{self.name} is open"
#         return msg

# restaurant = Restaurant("Papa Johns", "Pizza")
# print(restaurant.cuisine_type)
# print(restaurant.name)
# print(restaurant.describe_resturant())
# print(restaurant.open_restaurant())

# restaurant = Restaurant("China City", "Chinese food")
# print(restaurant.cuisine_type)
# print(restaurant.name)
# print(restaurant.describe_resturant())
# print(restaurant.open_restaurant())

# # 9-3
# class User:
#     def __init__(self, first_name, last_name, email, username):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.username = username

#     def describe_user(self):
#       summary = f"""
#       Name: {self.first_name} {self.last_name}
#       Email: {self.email}
#       Username: {self.username}
#       """
#       return summary

#     def greet_user(self):
#         greeting = f"Hello {self.first_name} {self.last_name}"
#         return greeting

# liam = User("Liam", "Arocho", "moose@live.com","MrMoose")
# print(liam.describe_user())
# print(liam.greet_user())
# print(liam.first_name)

# # 9-4
# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_resturant(self):
#         rest_name = f"{self.name}"
#         food_type = f"{self.cuisine_type}"
#         statement = f"Welcome to {rest_name.title()}, we sell {food_type} food."
#         return statement

#     def open_restaurant(self):
#         msg = f"{self.name} is open"
#         return msg
    
#     def set_number_served(self, update_number_served):
#         self.number_served = update_number_served

#     def increment_number_served(self, served):
#         self.number_served += served

# restaurant = Restaurant("Friday's", "American Food")
# print(restaurant.number_served)

# restaurant.number_served=1
# print(restaurant.number_served)

# restaurant.set_number_served(5)
# print(restaurant.number_served)

# restaurant.increment_number_served(10)
# print(restaurant.number_served)

# # 9-5
# class User:
#     def __init__(self, first_name, last_name, email, username):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.username = username
#         self.login_attempts = 0

#     def describe_user(self):
#       summary = f"""
#       Name: {self.first_name} {self.last_name}
#       Email: {self.email}
#       Username: {self.username}
#       """
#       return summary

#     def greet_user(self):
#         greeting = f"Hello {self.first_name} {self.last_name}"
#         return greeting
    
#     def increment_login(self):
#         self.login_attempts += 1 

#     def reset_login_attempts(self):
#         self.login_attempts = 0

# liam = User("liam", "arocho", "moose@tv.com", "MrMoose")

# liam.increment_login()
# liam.increment_login()
# liam.increment_login()

# print(f"{liam.login_attempts}")
# liam.reset_login_attempts()
# print(f"{liam.login_attempts}")

# # 9-6
# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_resturant(self):
#         rest_name = f"{self.name}"
#         food_type = f"{self.cuisine_type}"
#         statement = f"Welcome to {rest_name.title()}, we sell {food_type} food."
#         return statement

#     def open_restaurant(self):
#         msg = f"{self.name} is open"
#         return msg
    
#     def set_number_served(self, update_number_served):
#         self.number_served = update_number_served

#     def increment_number_served(self, served):
#         self.number_served += served

# class IceCreamStand(Restaurant):
#     def __init__(self, name, cuisine_type):
#         super().__init__(name, cuisine_type)
#         self.flavors = ["Strawberry", "Chocolate", "Vanilla"]

#     def icecream_flavors(self):
#         print(f"{self.flavors}")

# flavors = IceCreamStand("Dariy Queen", "Ice Cream")
# print(flavors.describe_resturant())
# flavors.icecream_flavors()

# # 9-7
# class User:
#     def __init__(self, first_name, last_name, email, username):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.username = username
#         self.login_attempts = 0

#     def describe_user(self):
#       summary = f"""
#       Name: {self.first_name} {self.last_name}
#       Email: {self.email}
#       Username: {self.username}
#       """
#       return summary

#     def greet_user(self):
#         greeting = f"Hello {self.first_name} {self.last_name}"
#         return greeting
    
#     def increment_login(self):
#         self.login_attempts += 1 

#     def reset_login_attempts(self):
#         self.login_attempts = 0

# class Admin(User):
#     def __init__(self, first_name, last_name, email, username):
#         super().__init__(first_name, last_name, email, username)
#         self.privileges = Privileges()

# class Privileges():
#     def __init__(self, privileges = []):
#         self.privileges = privileges

#     def show_privileges(self):
#         print("You have the following privileges")
#         for privilege in self.privileges:
#             print(f"\t{privilege}")

# liam = Privileges("Liam", "Arocho", "Moose@live.com", "MrMoose")
# liam.privileges = ["can add post", "can delete post", "can ban user"]
# print(liam.show_privileges())

# # 9-9
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

# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#     def __init__(self, battery_size=75):
#         """Initialize the battery's attributes."""
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
#             print(f"This car can go about {range} miles on a full charge.")

#     def upgrade_battery(self):
#         if self.battery_size != 100:
#             self.battery_size = 100

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)
#         self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# # 9-10
# import Resta

# wendys = Resta.Restaurant("Wendys", "Fast Food")
# print(wendys.describe_resturant())

# # 9-11
# from priv_admin import Admin

# liam = Admin("liam", "Arocho", "moose@live.com", "mrmoose")
# print(liam.describe_user())

# liam_prive = ["can reset passwords"]

# liam.privileges.privileges = liam_prive
# print(liam.privileges.show_privileges())

# # 9-12
# skip

# # 9-13
# from random import randint
# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         return randint(1, self.sides)
    

# dice = Die()
# print(dice.roll_die())

# # 9-14
# from random import choice

# lottery = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]

# winner = choice(lottery)

# for rando in lottery
# print(winner)

