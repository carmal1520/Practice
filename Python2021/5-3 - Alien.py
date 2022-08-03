# alien_color = 'red'
# if alien_color == 'green':
#     print("You just earned 5 points")

# alien_color = 'yellow'
# if alien_color == 'green':
#     print("You just earned 5 points")
# elif alien_color != 'green':
#     print("You just earned 10 points")

# alien_color = 'green'
# if alien_color == 'green':
#     print("You just earned 5 points")
# elif alien_color != 'green':
#     print("You just earned 10 points")

# age = 1
# if age < 2:
#     print("you are a baby")
# elif age <= 3:
#     print("You are a toddler")
# elif age <= 12:
#     print("You are a kid")
# elif age <= 19:
#     print("You are a teenager")
# elif age <= 64:
#     print("you are an adult")
# elif age >= 65:
#     print("You are an elder")

# favorite_fruits = ['strawberry', 'grape', 'orange']
# if 'strawberry' in favorite_fruits:
#     print("You really like strawberry's")
# if 'grape' in favorite_fruits:
#     print("Grapes are good for lunch")
# if 'orange' in favorite_fruits:
#     print("Only sometimes do we like them")
# if 'peach' in favorite_fruits:
#     print('These are ok')
# if 'pear' not in favorite_fruits:
#     print("You should try something new")

# 5-8

# usernames = []
# if usernames:
#     for x in usernames:
#         if x == "admin":
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print(f"Hello {x}, thank you for logging in again.")
# else:
#     print("we need to get some users")

# 5-10
# current_users = ['carleeto', 'jshadow', 'shadowstep', 'mrMoose', 'surshadow']
# new_users = ['static', 'summit1g', 'dr_disrespect', 'coh', 'jshadow']

# users_lower = [users.lower for users in current_users]
# for users in new_users:
#     if users.lower() in users_lower:
#         print(f"{users} is already in use")
#     else:
#         print(f"{users} is available")

# 5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else: 
        number <= 9
        print(f"{number}th")
