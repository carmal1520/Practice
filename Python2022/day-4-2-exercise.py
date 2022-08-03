# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
num_items = len(names)
random_name = random.randint(0, num_items - 1)
name = names[random_name]
print(f"{name} is going to buy the meal today!")

