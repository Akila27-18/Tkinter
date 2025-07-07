import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        for index in reversed(selected):  # Reverse to avoid shifting index issues
            task_listbox.delete(index)
    else:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

def toggle_task(event):
    index = task_listbox.curselection()
    if index:
        current_text = task_listbox.get(index)
        if current_text.startswith("✓ "):
            task_listbox.delete(index)
            task_listbox.insert(index, current_text[2:])
        else:
            task_listbox.delete(index)
            task_listbox.insert(index, "✓ " + current_text)

# Main window
root = tk.Tk()
root.title("Daily Task List Manager")
root.geometry("400x400")
root.resizable(False, False)

# Entry for task input
task_entry = tk.Entry(root, width=30)
task_entry.place(x=20, y=20)

# Add Task Button
add_button = tk.Button(root, text="Add Task", width=10, command=add_task, bg="lightgreen")
add_button.place(x=280, y=16)

# Listbox and Scrollbar
task_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=40, height=15)
task_listbox.place(x=20, y=60)

scrollbar = tk.Scrollbar(root)
scrollbar.place(x=360, y=60, height=245)

# Link scrollbar to listbox
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Delete Button
delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task, bg="salmon")
delete_button.place(x=130, y=330)

# Double-click to toggle completed
task_listbox.bind("<Double-Button-1>", toggle_task)

root.mainloop()
