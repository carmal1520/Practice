# people = []

# person = {
#     'first_name' : 'laim',
#     'last_name' : 'arocho',
#     'age' : 34,
#     'city' : 'virginia beach',
#  }

# people.append(person)

# person = {
#     'first_name' : 'eric',
#     'last_name' : 'broadnax',
#     'age' : 35,
#     'city' : 'chesapeake',
# } 
# people.append(person)

# person = {
#     'first_name' : 'Russ',
#     'last_name' : 'Wesh',
#     'age' : 36,
#     'city' : 'chesapeak',
# }
# people.append(person)

# for person in people:
#     name = f"{person['first_name'].title()} {person['last_name']}"
#     print(f'{name}')

# pets = []

# pet = {
#     'Type' : 'Dog',
#     'Owner' : 'Yvonne', 
# }

# pets.append(pet)

# pet = {
#     'Type' : 'Cat',
#     'Owner' : 'Carlos',
# }

# pets.append(pet)

# pet = {
#     'Type' : 'Bird',
#     'Owner' : 'Eric',
# }

# pets.append(pet)

# for pet in pets:
#     for key, value in pet.items():
#         print(f'{key}: {value}')

# favorite_places = {
#     'laim' : ['virginia', 'cheasapeake'],
#     'eric' : ['virginia', 'norfolk'],
#     'russ' : ['hawaii', 'honolulu', 'california'],
# }

# for name, places in favorite_places.items():
#     print(f'\n{name} has lived in the following places')
#     for place in places:
#         print(f'\t{place}')

# favorite_numbers = {
#     'liam' : [5, 8, 7],
#     'jordan' : [11, 12, 13],
#     'russ' : [36, 88, 99, 55],
#     'david' : [13, 1],
#     'shawn' : [27, 100, 300, 500, 700],
# }

# for key, values in favorite_numbers.items():
#     print(f"{key}'s favorite numbers are")
#     for x in values:
#         print(f'\t{x}')

# cities = {
#     'Tokyo' : {
#         'location' : 'Japan',
#         'population' : 1000000,
#         'fact' : 'best place to live',
#     },

#     'New York' : {
#         'location' : 'United states',
#         'population' : 4000000,
#         'fact' : 'has big apples',
#     },

#     'Virginia Beach' : {
#         'location' : 'United States',
#         'population' : 30000,
#         'fact' : 'near the ocean',
#     }
# }

# for name_city, info_city in cities.items():
#     print(f'\n\tName: {name_city}')
#     location = f"{info_city['location']}"
#     population = f"{info_city['population']}"
#     fact = f"{info_city['fact']}"

#     print(f"\tCounty: {location}")
#     print(f"\tPopulation: {population}")
#     print(f"\tFact: {fact}")

# number = input('Please enter a number: ')
# number = int(number)
# if number % 10 == 0:
#     print(f'{number} is a multiple of 10')
# else:
#     print(f'{number} is not a multiple of 10')

# prompt = "Please enter a pizza topping."
# prompt += "\nEnter 'quit' when you want to exit "
# message = ""

# while message.lower() != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# prompt = '\nPlease enter your age'
# prompt += "\nenter 'quit' when you want  to exit."
# prompt += '\n\t>> '

# while prompt.lower() != 'quit':
#     age = input(prompt)
#     age = int(age)
#     if age < 3:
#         print('The ticket is free')
#     elif age <= 12:
#         print('The ticket is $10')
#     else:
#         print('The ticket is $15')

# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input('Which mountain would you like to climb someday? ')

#     responses[name] = response
#     print(responses)

# sandwich_orders = ['pastrami','salami', 'turkey', 'pastrami', 'chicken', 'meatball', 'pastrami']
# finished_sandwiches = []

# print('we are out of pastrami')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')    

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f'{current_sandwich} is being made')
#     finished_sandwiches.append(current_sandwich)

# for finished_sandwich in finished_sandwiches:
#     print(f"\nHere is a list of completed sandwhich orders: {finished_sandwich}")

# responses = {}

# polling_status = True

# while polling_status:
#     person = input('\nWhat is your name? ')
#     dream = input('Where is your dream vacation ')

#     responses[person] = dream

#     repeat = input('Would you like to let someone else poll? ')
#     if repeat == 'no':
#         polling_status = False
    
#     for person, dream in responses.items():
#         print(f"{person} would like to visit {dream}")

# def display_message():
#     print("I learned how to make functions")

# display_message()

# def favorite_book(title):
#     print(f"My favorite book is {title.title()}")

# favorite_book('Jungle book')

# def make_shirt(size='large', message='I love python'):
#     print(f"The size of the shirt is {size} and the message on the shirt is {message}")

# make_shirt()
# make_shirt(size='medium', message='I Love python')

# def describe_city(name, country='Japan'):
#     print(f"{name.title()} is in {country.title()}.")

# describe_city('tokyo')
# describe_city('virginia beach', country='USA')
# describe_city('fussa')

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# def city_country(city, country):
#     full = f"{city}, {country}"
#     return full.title()

# test = city_country('TOKYO', 'JAPAN')
# print(test)

# test = city_country('Virginia Beach', 'united STATES')
# print(test)

# test = city_country('Hollywood', 'Florida')
# print(test)

# def make_album(artist_name, album_title, Song_number=None):
#     artist = {'Name' : artist_name, 'Title': album_title}
#     if Song_number:
#         artist['Song_number'] = Song_number    
#     return artist

# while True:
#     print("\nPlease enter an Artist Name, Title Album and Song number")
#     print("\n(Enter 'quit' anytime to quit)")
#     a_name = input("\nArtist Name: ")
#     if a_name.lower() == 'quit':
#         break
#     a_title = input("Album Title: ")
#     if a_title.lower() == 'quit':
#         break
#     s_number = input("Song Number: ")
#     if s_number.lower() == 'quit':
#         break

#     test = make_album(a_name, a_title, s_number)
#     print(test)

# def city_country(city, country):
#     message = f'"{city.title()} {country.title()}"'
#     print(message)
# city_country('Tyoko', 'japan')

# def make_album(artist_name, album_title, track_number=None):
#     x = {'Artist Name' : artist_name, 'Album Title' : album_title}
#     if track_number:
#         x['track_number'] = track_number
#     return x

# while True:
#     print("\nPlease enter an Artist Name, Album Name and Track Number.")
#     print("\n(Enter 'quit' to exit anytime)")
#     a_name = input("Artist Name: ")
#     if a_name.lower() == 'quit':
#         break
#     al_name = input("Album Name: ")
#     if al_name.lower() == 'quit':
#         break
#     track = input("Track Number: ")
#     if track.lower() == 'quit':
#         break
    
#     x = make_album(a_name, al_name, track)
#     print(x)


# def show_messages(texts):
#     for text in texts:
#         print(text)

# text_messages = ['I want pizza', 'I like food', 'I want to eat']
# show_messages(text_messages)

# def send_messages(sent_messages):
#     print("\nThe folowing messages have been sent:")
#     for sent_message in sent_messages:
#         print(sent_message)

# def show_messages(text_messages, sent_messages):
#     while text_messages:
#         unsent_message = text_messages.pop()
#         print(f"Sending Text: {unsent_message}")
#         sent_messages.append(unsent_message)


# sent_messages = []
# text_messages = ['I want pizza', 'I like food', 'I want to eat']

# show_messages(text_messages, sent_messages)
# send_messages(sent_messages)

# def sandwiches(size, *items):
#     print(f"You ordered a {size} Sandwhich with the following items: ")
#     for item in items:
#         print(f" {item}")

# sandwiches('Large', 'salami', 'lettuce', 'tomato')
# sandwiches('small', 'chicken')

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

# print(user_profile)


# def car_info(manufacturer, model_name, **kwargs):
#     car_dict = {
#         'manufacturer' : manufacturer.title(),
#         'model_name' : model_name.title(), 
#     }

#     for kwarg, value in kwargs.items():
#         car_dict[kwarg] = value

#     return car_dict

# car = car_info('mazda', 'mazda 3', color='gray', trim='basic')
# print(car)

# car = car_info('honda', 'accord', color='blue', trim='loaded')
# print(car)


# import printing_fucntions

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []



# printing_fucntions.print_models(unprinted_designs, completed_models)
# printing_fucntions.show_completed_models(completed_models)


# unwatched_anime = []
# watched_anime = []


# def anime_list(unwatched_anime, watched_anime):
#     print("\nPlease enter the name of an anime you want to watch")
#     print("\n(Please enter 'quit' to exit any time)")
#     while True:
#         a_name = input("Enter Anime Name: ")
#         if a_name.lower() == 'quit':
#             break
#         print(f"You want to watch: {a_name.title()}")
#         unwatched_anime.append(a_name)

#     while unwatched_anime:
#         current_anime = unwatched_anime.pop
#         print(f"You finished watching {current_anime.title()}")

# anime_list()      

# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type ):
#         """Initilize restaurant_name and cuisine_type attributes"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"\nThe restaurant is called {self.restaurant_name}")
#         print(f"\nWe serve {self.cuisine_type} type of cuisine.")

#     def open_restaurant(self):
#         print("The restaurant is open")

# rest_1 = Restaurant('Village Inn', 'American')
# print(rest_1.restaurant_name)
# print(rest_1.cuisine_type)

# rest_1.describe_restaurant()
# rest_1.open_restaurant()

# rest_2 = Restaurant("Wendys", "Fast Food")
# rest_2.describe_restaurant()

# rest_3 = Restaurant("PHO 79", "Vietnamese")
# rest_3.describe_restaurant()

# class User:

#     def __init__(self, first_name, last_name, birthday, email_address):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.birthday = birthday
#         self.email_address = email_address.lower()

#     def describe_user(self):
#         user_info = {
#             "First Name" : self.first_name,
#             "Last Name" : self.last_name,
#             "Birthday" : self.birthday,
#             "Email Address" : self.email_address,
#         }
#         for key, value in user_info.items():
#             print(f"{key} : {value}")
    
#     def greet_user(self):
#         greet = f"Hello: {self.first_name} {self.last_name}"
#         print(greet)

# user_1 = User("carlos", "maldonado", "February 14th", "coolcarlos@hotmail.com")
# user_1.describe_user()
# user_1.greet_user()

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         info = f"The Restaurant name is {self.restaurant_name} and sells {self.cuisine_type}"
#         print(info)

#     def open_restaurant(self):
#         info = f"{self.restaurant_name} is open"
#         print(info)

#     def set_number_served(self, number_served):
#         self.number_served = number_served

#     def increment_number_served(self, new_n):
#         self.number_served += new_n

# restaurant = Restaurant('Wendys', 'Fast Food')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.set_number_served(10)
# print(f" {restaurant.number_served}")

# restaurant.increment_number_served(5)
# print(f"{restaurant.number_served}")

# class User:
#     def __init__(self, first_name, last_name, username, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.email = email
#         self.login_atttempts = 0

#     def describe_user(self):
#         user_info = {
#             "First Name" : self.first_name,
#             "Last Name" : self.last_name,
#             "Username" : self.username,
#             "Email" : self.email,
#         }

#         for key, value in user_info.items():
#             print(f"{key} : {value}")

#     def greet_user(self):
#         msg = f"\nHello {self.first_name.title()} {self.last_name.title()}"
#         print(msg)

#     def increment_login_attempts(self):
#         self.login_atttempts += 1

#     def reset_login_attempts(self):
#         self.login_atttempts = 0

# user = User("Carlos", "Maldonado", "coolguy", "cool@hotmail.com")
# user.describe_user()
# user.greet_user()

# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(f"{user.login_atttempts}")

# user.reset_login_attempts()
# print(f" {user.login_atttempts}")

# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         message = f"Name: {self.restaurant_name} Cuisine Type: {self.cuisine_type}"
#         print(message)

#     def open_restaurant(self):
#         message = f"{self.restaurant_name.title()} is open and serving {self.cuisine_type}"
#         print(message)

#     def set_numbered_served(self, served):
#         self.number_served = served
    
#     def increment_number_served(self):
#         self.number_served += 1

# restaurant = Restaurant('Taco Bell', 'Fast Food')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant.set_numbered_served(40)
# print(restaurant.number_served)

# restaurant.increment_number_served()
# restaurant.increment_number_served()
# restaurant.increment_number_served()
# restaurant.increment_number_served()
# print(restaurant.number_served)

# class IceCreamStand(Restaurant):

#     def __init__(self, restaurant_name, cuisine_type='ice_cream'):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = []

#     def flavor(self):
#         for flavor in self.flavors:
#             print(flavor)

# straw = IceCreamStand("Ben and Jerry")
# straw.flavors = ['strawberry', 'vanilla', 'chocolate']

# straw.describe_restaurant()
# straw.flavor()

