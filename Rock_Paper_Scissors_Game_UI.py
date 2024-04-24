import random
import tkinter as tk
from tkinter import messagebox

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice):
    computer_choice = get_computer_choice()
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'User wins!'
    else:
        return 'Computer wins!'

# Function to play the game
def play_game(user_choice):
    result = determine_winner(user_choice)
    messagebox.showinfo("Result", result)

# Create the main window
root = tk.Tk()

# Create buttons for each choice
rock_button = tk.Button(root, text="Rock", command=lambda: play_game('rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'))

# Arrange the buttons in the window
rock_button.pack(side=tk.LEFT)
paper_button.pack(side=tk.LEFT)
scissors_button.pack(side=tk.LEFT)

# Start the main loop
root.mainloop()
