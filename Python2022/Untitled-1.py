# alien_color = "red"

# if alien_color == 'green':
#     print("you earned 5 points")
# elif alien_color == 'yellow':
#     print("you earned 10 points")
# else:
#     print("you eanred 15 points")

# 5-6
# age = 1
# if age < 2:
#     print("You are a baby")
# elif age < 4:
#     print("You are a toddler")
# elif age < 13:
#     print("You are a kid")
# elif age < 20:
#     print("You are a teenager")
# elif age < 65:
#     print("You an are adult")
# else:
#     print("You are an elder")

# 5-7
# favorite_fruits = ["orange", "grape", "strawberry"]
# if "orange" in favorite_fruits:
#     print("You like Oranges")

# 5-8
# usernames = ['admin', 'leeto', 'shadow', 'smoke', 'pwn']
# for username in usernames:
#     if username == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello, {username}, thank you for logging in agian.")

# 5-9
# usernames = []
# if usernames:
#     print('test')
# else:
#     print("we need to find some users.")

# 5-10
# current_users = ['leeto', 'meeto', 'eeto', 'ceto', 'peepo']
# new_users = ['leeto', 'eeto', 'coal', 'uwu', 'glide']

# for user in new_users:
#     if user.lower() in current_users:
#         print(f"{user} is already in use")
#     else:
#         print(f"{user} is available.")

# 5-11
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in numbers:
#     if number == 1:
#         print(f'{number}st')
#     elif number == 2:
#         print(f'{number}nd')
#     elif number == 3:
#         print(f'{number}rd')
#     elif number < 10:
#         print(f'{number}th')

# 6-1
# person = {
#     "First name" : "Liam",
#     "Last name" : "Arocho",
#     "Age" : 35,
#     "City" : "Chesapeake",
#     }

# print(person["First name"])
# print(person["Last name"])
# print(person["Age"])
# print(person["City"])

# 6-2
# number = {
#     "Carlos" : 19,
#     "Jon" : 20,
#     "Mike" : 12,
#     "Jose" : 32,
#     "Chris" : 3,
#     }

# num = number["Carlos"]
# print(f'Carlos favorite number is {num}')
# num = number["Chris"]
# print(f"Chris favorite number is {num}")

# 6-3
# glossary = {
#     "Cat" : "A small animal",
#     "Dog" : "A big animal",
#     }

# cat = glossary["Cat"]
# print(f'Cat : {cat}')

# 6-4
# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     'key': 'The first item in a key-value pair in a dictionary.',
#     'value': 'An item associated with a key in a dictionary.',
#     'conditional test': 'A comparison between two values.',
#     'float': 'A numerical value with a decimal component.',
#     'boolean expression': 'An expression that evaluates to True or False.',
#     }

# for key, value in glossary.items():
#     print(f'\n{key.title()} : {value}')

# 6-5
# rivers = {
#     "Nile" : "Africa",
#     "Amazon" : "Peru",
#     "Mississippi" : "US",
#     }
# for key, value in rivers.items():
#     print(f'The {key} river is located in {value.title()}')

# for key in rivers.keys():
#     print(f'The {key.title()} is a river')

# for value in rivers.values():
#     print(f'{value.title()} is a country')

# 6-6
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# poll = ["liam", "Carlos", "phil", "edward"]

# for name in poll:
#     if name in favorite_languages:
#         print(f'{name.title()}, thank you for taking the poll')
#     else:
#         print(f'{name.title()}, please take the poll')

# 6-7
# people = []

# liam = {
#     "First_name" : "Liam",
#     "Last_name" : "Arocho",
#     "Age" : 35,
#     "City" : "Chesapeake",
#     }
# people.append(liam)
# carlos = {
#     "First_name" : "Carlos",
#     "Last_name" : "Maldo",
#     "Age" : 35,
#     "City" : "Arlington",
# }
# people.append(carlos)
# jojo = {
#     "First_name" : "Jonathan",
#     "Last_name" : "jostar",
#     "Age" : 55,
#     "City" : "Anime world",
# }
# people.append(jojo)

# for person in people:
#     name = f'{person["First_name"].title()} {person["Last_name"].title()}'
#     print(name)

# 6-8
# pets = []

# animal = {
#     'name' : 'toto',
#     'type' : 'dog',
#     'owners_name' : 'ashely'
# }
# pets.append(animal)
# animal = {
#     'name' : 'leaf',
#     'type' : 'bird',
#     'owners_name' : 'ryan'
# }
# pets.append(animal)
# animal = {
#     'name' : 'fuji',
#     'type' : 'dog',
#     'owners_name' : 'carlos'
# }
# pets.append(animal)

# for pet in pets:
#     name = f"{pet['name'].title()}"
#     kind = f"{pet['type'].title()}"
#     owner = f"{pet['owners_name'].title()}"
#     print(f"{name} {kind} {owner}")

# 6-9
# favorite_places = {
#     "carlos" : ["japan", "thailand", "korea"],
#     "liam" : ["usa", "mexico"],
#     "ashely" : ["columbia"],
# }

# for key, value in favorite_places.items():
#     print(f"\n{key.title()}")
#     for v in value:
#         print(f"-{v.title()}")

# 6-10
# number = {
#     "Carlos" : [19, 20, 21],
#     "Jon" : [20, 32, 22,], 
#     "Mike" : [12, 13, 14],
#     "Jose" : [32, 77, 54],
#     "Chris" : [3],
#     }
# for key, value in number.items():
#     print(f"\n{key.title()}'s favorite number is")
#     for v in value:
#         print(f"-{v}")

# 6-11
# cities = {
#     "Tokyo" : {
#         "Country" : "Japan",
#         "Population" : 160_000_000,
#         "Fact" : "Known for great anime",
#     },

#     "Vegan" : {
#         "Country" : "Phillipines",
#         "Population" : 134_555_045,
#         "Fact" : "Known for good beaches",
#     },

#     "Virgina" : {
#         "Country" : "United States",
#         "Population" : 190_999_999,
#         "Fact" : "Known for great anime",
#     },
# }

# for key, value in cities.items():
#     print(f'{key.title()}')
#     for v in value.items():
#         print(f'\t{v}')

# 7-1
# message = input("What kind of car do you want? ")
# print(f'let see if we can find you a {message}')

# 7-2
# group = input("How many people are in the dinner party? ")
# group = int(group)
# if group > 8:
#     print("Youll have to wait for a table.")
# else:
#     print("Your table is ready")

# 7-3
# number = input("Give me a number: ")
# number = int(number)
# if number % 2 == 0:
#     print(f'{number} is a multiple of 10')
# else:
#     print(f'{number} is not a multple of 10')

# 7-4
# toppings = input("Enter a pizza topping")
# toppings += input("Enter 'quit' to exit")

# while True:
#     pt = toppings

#     if toppings == 'quit':
#         break
#     else:
#         print(f"{pt} has been added to the pizza.")

# 7-5
# prompt = "How old are you? "
# prompt += "Type 'quit' to exit"

# while True:
#     age = int(prompt)
#     if age 
#     if age < 3:
#         print("The ticket is free")
#     elif age < 12:
#         print("The ticket is $10")
#     else:
#         print('The ticket is $15.')

# 7-8
# sandwich_orders = ['salami', 'turkey', 'blt', 'steak']
# finished_sandwiches = []
# while sandwich_orders:
#     new_order = sandwich_orders.pop()
#     print(f'\nI made your {new_order} sandwich.')
#     finished_sandwiches.append(new_order)

# print("\nThe following sandwiches have been made:")
# for x in finished_sandwiches:
#     print(f'\t{x} sandwich')

# 7-9
# sandwich_orders = ['pastrami', 'salami', 'pastrami', 'turkey', 'blt', 'steak', 'pastrami']
# finished_sandwiches = []

# print("We've run out of pastrami sandwiches")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     new_order = sandwich_orders.pop()
#     print(f'\nI made your {new_order} sandwich.')
#     finished_sandwiches.append(new_order)

# print("\nThe following sandwiches have been made:")
# for x in finished_sandwiches:
    # print(f'\t{x} sandwich')

# 7-10
# poll = {}

# prompt = "If you could visit a place in the world, where would you go?"
# prompt += "\nType 'quit' to escape: "

# poll_active = True

# while poll_active:
#     answer = input(prompt)
#     name = input("What is your name? ")
#     poll[name] = answer

#     repeat = input('Would you like to let another person respond? (yes/no)')
#     if repeat == 'no':
#         poll_active = False
# print('\n---Poll Results---')
# for name, answer in poll.items():
#     print(f'{name.title()} wants to visit {answer}')

# 8-1
# def display_message():
#     print("I learned about functions")

# display_message()

# 8-2
def favorite_book(title):
    msg = f'My favorite book is {title.title()}'
    print(msg)
favorite_book("anime")
