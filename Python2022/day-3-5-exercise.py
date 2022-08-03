# 🚨 Don't change the code below 👇
from traceback import print_tb


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowername1 = name1.upper()
lowername2 = name2.upper()

# words = ["L", "O", "V", "E", "T", "R", "U", "E"]

lname1 = 0
lname2 = 0
love_score = lname1 + lname2

if lowername1.count("L"):
    lname1 +=1
if lowername1.count("O"):
    lname1 +=1
if lowername1.count("V"):
    lname1 +=1
if lowername1.count("E"):
    lname1 +=1
if lowername1.count("T"):
    lname1 +=1
if lowername1.count("R"):
    lname1 +=1
if lowername1.count("U"):
    lname1 +=1
if lowername1.count("E"):
    lname1 +=1

if lowername2.count("L"):
    lname2 +=1
if lowername2.count("O"):
    lname2 +=1
if lowername2.count("V"):
    lname2 +=1
if lowername2.count("E"):
    lname2 +=1
if lowername2.count("T"):
    lname2 +=1
if lowername2.count("R"):
    lname2 +=1
if lowername2.count("U"):
    lname2 +=1
if lowername2.count("E"):
    lname2 +=1

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")