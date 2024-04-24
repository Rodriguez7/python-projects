import tkinter as tk
import winsound

# Variables to keep track of the state
focus_time = 25*60
short_break_time = 5*60
long_break_time = 15*60
pomodoros_completed = 0
timer_running = False
remaining_time = focus_time

# Function to update the timer
def update_timer():
    global remaining_time, timer_running
    if timer_running and remaining_time > 0:
        remaining_time -= 1
        # Format the time as mm:ss
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        # Update the label with the time
        timer_label.config(text=time_string)
        # Schedule the next update
        root.after(1000, update_timer)
    elif timer_running and remaining_time == 0:
        # Play a sound when the timer ends
        winsound.Beep(440, 500)  # Beep at 440 Hz for 500 ms
        start_break()

# Function to start a break
def start_break():
    global pomodoros_completed, remaining_time
    # Increment the number of completed Pomodoros
    pomodoros_completed += 1
    # If four Pomodoros have been completed, start a long break
    if pomodoros_completed % 4 == 0:
        remaining_time = long_break_time
    # Otherwise, start a short break
    else:
        remaining_time = short_break_time
    update_timer()

# Function to start the timer
def start_timer():
    global timer_running, remaining_time
    remaining_time = focus_time
    timer_running = True
    update_timer()

# Function to pause or resume the timer
def pause_or_resume_timer():
    global timer_running
    if timer_running:
        timer_running = False
    else:
        timer_running = True
        update_timer()


# Function to reset the timer
def reset_timer():
    global timer_running, remaining_time, pomodoros_completed
    timer_running = False
    remaining_time = focus_time
    pomodoros_completed = 0
    timer_label.config(text="25:00")

# Create the main window
root = tk.Tk()
root.title("Pomodoro Timer")

# Create a label to display the timer
timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
timer_label.pack()

# Create buttons for each operation
start_button = tk.Button(root, text="Start Pomodoro", command=start_timer)
pause_button = tk.Button(root, text="Pause/Resume", command=pause_or_resume_timer)
reset_button = tk.Button(root, text="Reset", command=reset_timer)

# Arrange the buttons in the window
start_button.pack(side=tk.LEFT, padx=5)
pause_button.pack(side=tk.LEFT, padx=5)
reset_button.pack(side=tk.LEFT, padx=5)

# Start the main loop
root.mainloop()
