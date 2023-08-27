import random


while True:

    random_number = random.randint(1, 100)
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):

        guess = input("Enter your guess (1-100) or press 'q' to quit [Attempt {}/{}]: ".format(attempt, max_attempts))


        if guess.lower() == 'q':
            print("Quitting the game. The number was {}.".format(random_number))
            break


        if not guess.isdigit():
            print("Please enter a valid number.")
            continue


        guess = int(guess)


        if guess == random_number:
            print("Congratulations! You've guessed the correct number.")
            break
        elif guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    else:

        print("Sorry, you've reached the maximum number of attempts. The correct number was {}.".format(random_number))


    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != 'y':
        print("Thanks for playing! Goodbye.")
        break