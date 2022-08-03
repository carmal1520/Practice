# # 10-3
# question = input("What is your name? ")

# with open('guest.txt', 'w') as file_object:
#     file_object.write(question)

# # 10-4
# while True:
#     name = input("What is your name? ")
#     if name == 'quit':
#         break
#     else:
#         with open('guest_book.txt', "a") as file_object:
#             file_object.write(name)

# # 10-5
# while True:
#     question = input("Why do you like programming? ")
#     if question == 'quit':
#         break
#     else:
#         with open('poll.txt', 'a') as x:
#             x.write(f"{question}\n")

# # 10-6
# print("Give me two numbers and i will add them.")
# print("press 'q' to quit")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
    
#     else:
#         try:
#             answer = int(first_number) + int(second_number)
#             print(answer)
#         except ValueError:
#             print("Please enter a number")

# try:
#     x = input("Give me a number: ")
#     x = int(x)

#     y = input("Give me another number: ")
#     y = int(y)
# except ValueError:
#     print("Sorry, I really needed a number.")
# else:
#     sum = x + y
#     print(f"The sum of {x} and {y} is {sum}.")

# # 10-7
# same as 10-6

# # 10-8
# name = input('Enter a Dog name: ')
# with open('dogs.txt', 'a') as x:
#     x.write(f"{name}\n")

# try:
#     with open('gd.txt') as x:
#         contents = x.read()
#         print(contents)
# except FileNotFoundError:
#     print("That file is missing")

# # 10-9
# just add 'pass' to except

# # 10-10
# with open('japan.txt', encoding='utf-8') as x:
#     y = x.read()
#     the = y.lower().count('the')
#     print(the)

# # 10-11
# import json
# number = input("Whats your favorite number? ")

# with open('favorite_number.json', 'w') as f:
#     json.dump(number, f)

# import json
# with open('favorite_number.json') as f:
#     number = json.load(f)

# print(number)

# # 10-12
# import json
# try:
#     with open('favorite_number.json') as f:
#         number = json.load(f)
# except FileNotFoundError:
#     number = input("Enter your favorite number")
#     with open('favorite_number.json', 'w') as f:
#         json.dump(number, f)
#     print(f"Your favorite number is {number}")
# else:
#     print(f"Your favorite number is {number}")
