import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("350x400")

# Task Entry
tk.Label(root, text="Enter a task:").pack(pady=5)
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Task Listbox
tk.Label(root, text="Current Tasks:").pack(pady=5)
task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=5)

# Remove Task Button
remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task)
remove_button.pack(pady=10)

root.mainloop()
