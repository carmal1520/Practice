import json

try:
    with open("favorite_number.json") as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Whats your favorite Number? ")
    with open("favorite_number.json", "w") as f:
        json.dump(number, f)
        print("You favorite number has been saved.")
else:
    print(f"Your favorite number was {number}") 