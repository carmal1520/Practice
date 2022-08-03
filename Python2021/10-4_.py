filename = 'guest_book.txt'

while True:
    name = input("What is your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as x:
            x.write(f"{name}\n")
        print(f"Hello {name}, you have been added to the guest book.")

        