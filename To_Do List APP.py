import tkinter as tk
from tkinter import simpledialog, messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a listbox to display the tasks
tasks = tk.Listbox(root, width=50, height=10)
tasks.pack(pady=10)

# Function to add a task
def add_task():
    task = simpledialog.askstring("Add task", "Enter task:")
    if task is not None:
        tasks.insert(tk.END, task)

# Function to edit a task
def edit_task():
    selected_task_index = tasks.curselection()
    if not selected_task_index:
        messagebox.showinfo("Edit task", "No task selected!")
        return
    old_task = tasks.get(selected_task_index)
    new_task = simpledialog.askstring("Edit task", "Edit task:", initialvalue=old_task)
    if new_task is not None:
        tasks.delete(selected_task_index)
        tasks.insert(selected_task_index, new_task)

# Function to delete a task
def delete_task():
    selected_task_index = tasks.curselection()
    if not selected_task_index:
        messagebox.showinfo("Delete task", "No task selected!")
        return
    tasks.delete(selected_task_index)

# Create buttons for each operation
add_button = tk.Button(root, text="Add Task", command=add_task)
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)

# Arrange the buttons in the window
add_button.pack(side=tk.LEFT, padx=5)
edit_button.pack(side=tk.LEFT, padx=5)
delete_button.pack(side=tk.LEFT, padx=5)

# Start the main loop
root.mainloop()
