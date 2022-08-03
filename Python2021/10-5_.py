filename = "reason.txt"

print("Enter 'quit' to exit")

while True:
    responses = input("Why do you like programming? ")
    if responses == 'quit':
        break
    else:
        with open(filename, 'a') as x:
           x.write(f"{responses}\n")
        print("Your response has been recorded")
