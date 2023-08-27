#unlimited guess until guessed it right.

import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

while True:
    # Get the player's guess
    guess = input("Enter your guess (1-100) or press 'q' to quit: ")

    # Check for quit command
    if guess.lower() == 'q':
        print("Quitting the game. The number was {}.".format(random_number))
        break

    # Check if the input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    # Convert the guess to an integer
    guess = int(guess)

    # Check the guess
    if guess == random_number:
        print("Congratulations! You've guessed the correct number.")
        break
    elif guess < random_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
