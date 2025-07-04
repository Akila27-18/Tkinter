import tkinter as tk
from tkinter import messagebox, filedialog

# Add a new task
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

# Mark task as done/undone on double-click
def toggle_done(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        if task.startswith("✓ "):
            listbox.delete(index)
            listbox.insert(index, task[2:])  # remove ✓
        else:
            listbox.delete(index)
            listbox.insert(index, "✓ " + task)  # add ✓

# Save tasks to file
def save_tasks():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "w") as f:
            tasks = listbox.get(0, tk.END)
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully!")

# Load tasks from file
def load_tasks():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "r") as f:
            listbox.delete(0, tk.END)
            for line in f:
                listbox.insert(tk.END, line.strip())

# --- GUI setup
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x450")

# Top Frame for Entry and Button
frame_top = tk.Frame(root, pady=10)
frame_top.pack()

entry = tk.Entry(frame_top, width=30)
entry.pack(side=tk.LEFT, padx=5)

btn_add = tk.Button(frame_top, text="Add Task", command=add_task)
btn_add.pack(side=tk.LEFT)

# Middle Frame for Listbox + Scrollbar
frame_list = tk.Frame(root)
frame_list.pack(padx=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_list, height=15, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Double-click binding
listbox.bind("<Double-Button-1>", toggle_done)

# Bottom Frame for Save/Load
frame_bottom = tk.Frame(root, pady=10)
frame_bottom.pack()

btn_save = tk.Button(frame_bottom, text="Save List", command=save_tasks, width=15)
btn_save.pack(side=tk.LEFT, padx=5)

btn_load = tk.Button(frame_bottom, text="Load List", command=load_tasks, width=15)
btn_load.pack(side=tk.LEFT, padx=5)

root.mainloop()
