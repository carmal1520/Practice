print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you liek to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
tip = percent / 100
result = (bill / split) * tip
print(f"Each person should pay ${result}")