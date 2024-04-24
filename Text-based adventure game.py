import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Initialize the guess to None
    guess = None

    # Game loop
    while guess != number_to_guess:
        # Get the user's guess
        guess = int(input("Guess a number between 1 and 100: "))

        # Check if the guess is too high, too low, or correct
        if guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Congratulations! You guessed the number.")

# Start the game
guess_the_number()
