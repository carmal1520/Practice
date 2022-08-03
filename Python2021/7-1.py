# 7-1
# car = input("What kind of rental car would you like? ")
# print(f"\nLet me get the {car} out for you.")

# 7-2
# party = input("How many people are in the party? ")
# party = int(party)
# if party > 8:
#     print("You will have to wait for a table.")
# else:
#     print("Your table is ready.")

# 7-3
# number = input("Please type in a number: ")
# number = int(number)
# if number % 10 == 0:
#     print(f"{number} is a multiple of 10!")
# else:
#     print(f"{number} is not a multiple of 10!")

# 7-4
# prompt = "\n Please enter the toppings you want on your pizza "
# prompt += "\n Please enter 'QUIT' when you are finished: "

# while True:
#     toppings = input(prompt).lower()
#     if toppings != 'quit':
#         print(f"\n {toppings} has been added to your pizza")
#     else:
#         break

# 7-5
# prompt = "\n Please enter your age: "
# while True:
#     age = input(prompt).lower()
#     if age == 'quit':
#         break
#     age = int(age)
#     if age < 3:
#         print("The ticket is free")
#     elif age <= 12:
#         print("The ticket is $10")
#     elif age > 12:
#         print("The ticket is $15")

# 7-6
# prompt = "\n Please enter your age: "
# active = True
# while active:
#     age = input(prompt).lower()
#     if age == 'quit':
#         active = False
#     age = int(age)
#     if age < 3:
#         print("The ticket is free")
#     elif age <= 12:
#         print("The ticket is $10")
#     elif age > 12:
#         print("The ticket is $15")

#         prompt = "\n Please enter your age: "

# while True:
#     age = input(prompt).lower()
#     if age == 'quit':
#         break
#     age = int(age)
#     if age < 3:
#         print("The ticket is free")
#     elif age <= 12:
#         print("The ticket is $10")
#     elif age > 12:
#         print("The ticket is $15")

# 7-7
number = 1
while number > 5:
    print("KEKW")