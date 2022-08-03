# 7-8
# sandwich_orders = ['Grilled Cheese Sandwich', 'Egg and Bacon Sandwich', 'Chicken Sandwich']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"\nSandwich currently being made: {current_sandwich.title()}")
#     finished_sandwiches.append(current_sandwich)
# print("\nThe following sandwiches have been made:")
# for finished_sandwich in finished_sandwiches:
#      print(f"\t{finished_sandwich.title()}")

# 7-9
# sandwich_orders = ['Grilled Cheese Sandwich', 'Egg and Bacon Sandwich', 'Chicken Sandwich', 'pastrami', 'pastrami', 'pastrami']
# finished_sandwiches = []

# print("We are out of pastrami")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"\nSandwich currently being made: {current_sandwich.title()}")
#     finished_sandwiches.append(current_sandwich)

# print("\nThe following sandwiches have been made:")
# for finished_sandwich in finished_sandwiches:
#      print(f"\t{finished_sandwich.title()}")

# 7-10

dream_vacations = {}
polling_active = True
prompt = "Where is your dream vacation? "
while polling_active:
    dream = input(prompt)
    dream_vacations[dream] = dream
    repeat = input("Would you like to list another location? (yes/no)")
    if repeat == 'no':
        polling_active = False
    for location in dream_vacations:
        print(f"\t These are the listed vacation spots: {location.title()}")