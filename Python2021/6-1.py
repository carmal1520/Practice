# person = {'first_name' : 'Liam', 
# 'last_name' : 'arocho', 
# 'city' : 'virginia beach'}
# x = person['city'].title()
# print(person['first_name'])
# print(person['last_name'])
# print(f"my friend lives in {x}")

# 6-2
# fav_number = {'carlos' : 14, 'jordan' : 29, 'laim' : 77, 'russ' : 12, 'eric' : 90}
# x = fav_number.items()
# for items in x:
#     print(items)

# 6-3
# glossary = {'dictionary' : 'collection of key-value pairs',
# 'conditional test' : 'an expression that can be evaluated as True or False',
# 'list' : 'an ordered and mutable python container',
# 'index' : 'the poistion of a value in a list',
# 'variable' : 'a reserved memory location to store values'}

# for x, y in glossary.items():
#     print(f'{x.title()} : {y.title()}')

 #  6-5
# rivers = {'nile' : 'africa', 'amazon' : 'peru', 'yenisei' : 'russia'}
# for x in sorted(rivers):
#     print(x.title())
# for x in sorted(rivers.values()):
#     print(f'\n{x.title()}')
# for x, y in sorted(rivers.items()):
#     print(f'\n{x.title()} orginates from {y.title()}')

# 6-6
# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ruby',
#     'phil' : 'python',
# }
# for x in favorite_languages:
#      print(f"{x}, thank you for voting")

# people = ['jen', 'edward', 'liam', 'jordan']
# for x in people:
#     if x not in favorite_languages:
#      print(f'{x}, get out and vote!')

# alien_0 = dict(color='green', points=5)
# alien_1 = dict(color='yellow', points=10)
# alien_2 = dict(color='red', points=15)

# aliens = [alien_0, alien_1, alien_2]

# for alien  in aliens:
#     print(alien)

# aliens = []

# for alien_number in range(10):
#     new_alien = dict(color='green', points=5, speed='slow')
#     aliens.append(new_alien)

# for alien in aliens:
#     print(alien)
# print(f'Total number of aliens: {len(aliens)}')

# 6-7
# people = []

# person = {
#     'first_name' : 'Liam', 
#     'last_name' : 'arocho', 
#     'city' : 'virginia beach'
# }
# people.append(person)

# person = {
#     'first_name' : 'Jordan',
#     'last_name' : 'wesh', 
#     'city' : 'maryland'
# }
# people.append(person)

# person = {
#     'first_name' : 'eric', 
#     'last_name' : 'broadnax', 
#     'city' : 'virginia beach'
# }
# people.append(person)

# for person in people:
#     name = f"{person['first_name'].title()} {person['last_name'].title()}"
#     city = f"{person['city'].title()}"
#     print(f"My friend {name} is from {city}")

# 6-8

# pets = []

# pet = {
#     'type' : 'chihuahua',
#     'owner': 'carlos',
# }
# pets.append(pet)

# pet = {
#     'type' : 'rottweiler',
#     'owner': 'yvonne',
# }
# pets.append(pet)

# pet = {
#     'type' : 'dobermann',
#     'owner' : 'Jr'
# }
# pets.append(pet)

# for pet in pets:
#     for key, vaule in pet.items():
#         print(f"\n{key} : {vaule}")

    # type = f"{pet['type'].title()}"
    # owner = f"{pet['owner'].title()}"
    # print(f"{owner} owns a {type}")

# 6-9
    
# favotie_places = {
#     'carlos' : ['japan'],
#     'laim' : ['scotland', 'brazil', 'australia'],
#     'eric' : ['mexico', 'DC']
# }

# for x, y in favotie_places.items():
#     print(f"\n{x.title()}'s favorite places to go are:")
#     for z in y:
#         print(z)

# 6-10
# fav_number = {
#     'carlos' : [14, 34, 7],
#     'jordan' : [29, 18], 
#     'laim' : [77, 21, 99, 150],
#     'russ' : [12, 1000, 22, 1],
#     'eric' : [90, 80],
#     }
# for x, y in fav_number.items():
#     print(f"{x.title()}'s favorite numbers are :")
#     for z in y:
#         print(f"\t{z}")

# 6-11
# cities = {
#     'new york' : {
#         'country' : 'United States',
#         'population' : 1000000,
#         'fact' : 'Known as the big apple',
#     },
#     'los angeles' : {
#         'country' : 'United States',
#         'population' : 200000,
#         'fact' : 'homeless capital of America'
#     },
#     'tokyo' : {
#         'country' : 'Japan',
#         'population' : 999999999,
#         'fact' : "Has a sakura blossom festival"
#     },
# }
# for location, info in cities.items():
#     print(f"\n{location.title()}")
#     pop = f"{info['population']}"
#     fact = f"{info['fact']}"
#     country = f"{info['country']}"
#     print(f"\tCountry: {country.title()}")
#     print(f"\tPopulation: {pop}")
#     print(f"\tFact: {fact}")

# 6-12
school = {
    'Student 1' : {
        'name' : 'Carlos',
        'Grades' : [88, 90, 100],
        'Subject' : 'Science'
    },
    'Student 2' : {
        'name' : 'Liam',
        'Grades' : [44, 30, 5],
        'Subject' : 'Computer Science'
    },
    'Student 3' : {
        'name' : 'Jordan',
        'Grades': [75, 91, 2, 170],
        'Subject' : 'History',
    },
}

for students, subjects in school.items():
    name = f"{subjects['name']}"
    grade = f"{subjects['Grades']}"
    subject = f"{subjects['Subject']}"
    print(f"\nThe report card will be sent out for the following students:")
    print(f"\tID: {students}")
    print(f"\tName: {subjects['name']}")
    print(f"\t\tSubject: {subjects['Subject']}")
    print(f"\t\tGrades: {subjects['Grades']}")
