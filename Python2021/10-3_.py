name = input("What is your name? ")

with open('guest.txt', 'w') as x:
    x.write(name)
