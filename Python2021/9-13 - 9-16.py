# 9-13

# from random import randint

# class Die():
#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         return randint(1, self.sides)

# dice = Die()
# results = []

# for roll_num in range(10):
#     result = dice.roll_die()
#     results.append(result)

# print(results)

# 9-14
from random import choice
winner = []
lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]
random = choice(lotto)
for pick in range(4):
    result = random
    winner.append(result)
print(winner)