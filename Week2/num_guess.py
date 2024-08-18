import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("You have 3 attempts to guess the number between 1 and 10.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number!")
            return
        elif guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")


    print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")

number_guessing_game()