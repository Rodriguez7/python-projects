import tkinter as tk

# Function to evaluate the expression in the entry field
def evaluate(event):
    try:
        result = eval(entry.get())
        label.config(text = "Result: " + str(result))
    except:
        label.config(text = "Invalid expression")

# Create a new window
window = tk.Tk()
window.title("Calculator")

# Create an entry field
entry = tk.Entry(window, width=20)
entry.bind("<Return>", evaluate)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, command=lambda button=button: entry.insert(tk.END, button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a label to display the result
label = tk.Label(window, text="Result:")
label.grid(row=row_val+1, column=0, columnspan=4)

window.mainloop()