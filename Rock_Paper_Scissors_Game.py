import random

# Function to get the computer's choice
def get_computer_choice():
    # List of possible choices
    choices = ['rock', 'paper', 'scissors']
    # Return a random choice
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    # If both choices are the same, it's a tie
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    # User wins if they chose rock and computer chose scissors,
    # or user chose scissors and computer chose paper,
    # or user chose paper and computer chose rock
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'User wins!'
    # If none of the above conditions are met, the computer wins
    else:
        return 'Computer wins!'

# Function to play the game
def play_game():
    # Get the user's choice
    user_choice = input('Enter your choice (rock, paper, scissors): ')
    # Get the computer's choice
    computer_choice = get_computer_choice()
    # Print the computer's choice
    print('Computer chose:', computer_choice)
    # Determine and print the winner
    print(determine_winner(user_choice, computer_choice))

# Call the function to start the game
play_game()
