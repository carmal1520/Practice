import json

number = input("Whats your favorite Number? ")
with open("favorite_number.json", "w") as f:
    json.dump(number, f)
    print("You favorite number has been saved.")