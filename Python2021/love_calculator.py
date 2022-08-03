# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
love = ["T", "R", "U", "E", "L", "O", "V", "E"]
name_list = []
count = []

for x in range(0, len(name1)):
    name_list.append(name1[x])

for letters in name_list:
    if letters in love:
        count += 1
    print((count))
# for x in range(0, len(name2)):
#     name_list.append(name2[x])   
