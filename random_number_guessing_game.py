# This script is a random number guessing game where the computer chooses a random number between 1 and 100.
# The user is prompted to guess the number, and the script provides feedback if the guess is too low, too high, or correct.
# It also ensures that the user input is a valid number and that the guess is within the range of 1 to 100.
# The game tracks the number of guesses and ends when the user correctly guesses the number.

# Creates a random number generation tool
import random

# Defines the main function for the program
def main():
    # Chooses a random number between 1 and 100
    RandomNum = random.randint(1, 100) ## ".randint(1, 100)" picks a random integer between 1 and 100

    print("I've thought of a number from 1 through 100")

    # This creates a track record for the number of guesses
    NumGuesses = 0

    # Creates a loop in which only ended when the guess is correct
    while True:
        # Ask the user for their guess
        guess = input("Guess the number: ")

        # Makes sure the user entered an integer and nothing else
        if not guess.isdigit(): ## ".isdigit()" takes the number given by "guess" and dictates whether it is a number or not
            print("You did not enter a number")
            continue

        # Converts the guess to an integer
        guess = int(guess)

        # Makes sure the guess is between 1 and 100
        if guess < 1 or guess > 100:
            print("Number must be from 1 through 100")
            continue

        # Increases the guess count for each guess
        NumGuesses += 1

        # Checks if the user's guess is correct
        if guess == RandomNum:
            print("Correct! You took", NumGuesses,"guesses")
            break
        elif guess < RandomNum:
            print("Too low")
        else:
            print("Too high")

# Starts the game
main()
