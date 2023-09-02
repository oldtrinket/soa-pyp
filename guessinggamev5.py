import random

messages = {}
with open("messages.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "=" in line:
            key, value = line.strip().split('=')
            messages[key] = value

while True:
    random_number = random.randint(1, 100)
    max_attempts = 5
    guesses = []

    for attempt in range(1, max_attempts + 1):
        guess = input(messages["GUESS_PROMPT"].format(attempt, max_attempts))

        if guess.lower() == 'q':
            print(messages["QUIT_MESSAGE"].format(random_number))
            break

        if not guess.isdigit():
            print(messages["INVALID_NUMBER_MESSAGE"])
            continue

        guess = int(guess)
        guesses.append(guess)

        if guess == random_number:
            print(messages["CONGRATS_MESSAGE"])
            print(messages["GUESSES_HISTORY_MESSAGE"].format(guesses))
            break
        elif guess < random_number:
            print(messages["TOO_LOW_MESSAGE"])
        else:
            print(messages["TOO_HIGH_MESSAGE"])
    else:
        print(messages["MAX_ATTEMPTS_MESSAGE"].format(random_number))
        print(messages["GUESSES_HISTORY_MESSAGE"].format(guesses))

    replay = input(messages["REPLAY_PROMPT"]).lower()
    if replay != 'y':
        print(messages["GOODBYE_MESSAGE"])
        break
