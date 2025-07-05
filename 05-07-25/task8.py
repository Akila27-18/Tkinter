import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "Task cannot be empty.")
        return

    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        return

    task_listbox.delete(selected[0])

def mark_done(event):
    try:
        index = task_listbox.nearest(event.y)
        task_text = task_listbox.get(index)

        # Skip marking empty or already marked tasks
        if not task_text.strip():
            return

        if task_text.startswith("✔ "):
            # Unmark
            new_text = task_text.replace("✔ ", "", 1)
        else:
            new_text = f"✔ {task_text}"

        task_listbox.delete(index)
        task_listbox.insert(index, new_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main Window
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

# Entry + Add Button
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Frame for Listbox and Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
task_listbox = tk.Listbox(list_frame, width=40, height=15, yscrollcommand=scrollbar.set)
task_listbox.pack()
scrollbar.config(command=task_listbox.yview)

# Bind left-click to mark task done
task_listbox.bind("<Button-1>", mark_done)

# Delete Button
delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack(pady=10)

root.mainloop()
