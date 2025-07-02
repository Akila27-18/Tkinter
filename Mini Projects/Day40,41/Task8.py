import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry_task.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        task_listbox.delete(0, tk.END)
        save_tasks()

# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Entry
entry_task = tk.Entry(root, width=25)
entry_task.pack(pady=10)

# Listbox
task_listbox = tk.Listbox(root, width=40, height=15)
task_listbox.pack()

# Buttons
tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", width=20, command=delete_task).pack(pady=5)
tk.Button(root, text="Clear All", width=20, command=clear_all).pack(pady=5)

# Load saved tasks
load_tasks()

root.mainloop()
