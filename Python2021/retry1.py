#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from operator import truediv
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty, Type 'easy' or 'hard: ").lower()
computer_guess = random.randint(1, 100)
guess = int(input("Make a guess: "))
is_game_over = False
attempts = 0

if difficulty == "easy":
    attempts == 10
else:
    attempts == 5

def game():
    if guess > computer_guess:
        print("Too High")
    elif guess < computer_guess:
        print("Too low")

while True:
    if guess == computer_guess:
        print("You Win!")
        break
    else:
        attempts -= 1
        print("Guess again")
        print(f"You have {attempts} remaining to guess the number.")
        game()

    # if attempts == 0:
    #     print("You've run out of guesses, you lose.")
