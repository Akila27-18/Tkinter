import tkinter as tk
from tkinter import messagebox, filedialog

tasks = []

def refresh_list():
    task_listbox.delete(0, tk.END)
    for t in tasks:
        task_listbox.insert(tk.END, f"{t['name']} (Due: {t['deadline']})")

def open_add_task_dialog():
    def add_task():
        name = task_name.get().strip()
        deadline = task_deadline.get().strip()
        if not name:
            messagebox.showwarning("Missing", "Task name is required.")
            return
        tasks.append({"name": name, "deadline": deadline})
        refresh_list()
        dialog.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("Add New Task")
    dialog.geometry("300x150")
    dialog.transient(root)
    dialog.grab_set()

    tk.Label(dialog, text="Task Name:").pack(pady=5)
    task_name = tk.Entry(dialog)
    task_name.pack(pady=5)

    tk.Label(dialog, text="Deadline:").pack(pady=5)
    task_deadline = tk.Entry(dialog)
    task_deadline.pack(pady=5)

    tk.Button(dialog, text="Add Task", command=add_task).pack(pady=10)

def delete_task():
    if not task_listbox.curselection():
        messagebox.showwarning("Select Task", "Please select a task to delete.")
        return
    index = task_listbox.curselection()[0]
    if messagebox.askyesno("Confirm", "Delete this task?"):
        tasks.pop(index)
        refresh_list()

def save_tasks():
    if not tasks:
        messagebox.showinfo("No Tasks", "No tasks to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            for t in tasks:
                f.write(f"{t['name']} - Due: {t['deadline']}\n")
        messagebox.showinfo("Saved", f"Task list saved to:\n{file_path}")

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.quit()

# --- Main Window ---
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("600x400")

# --- Menu Bar ---
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Save List", command=save_tasks)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# --- Toolbar ---
toolbar = tk.Frame(root, bg="#ddd")
toolbar.pack(side="top", fill="x")

tk.Button(toolbar, text="Add Task", width=10, command=open_add_task_dialog).pack(side="left", padx=4, pady=4)
tk.Button(toolbar, text="Delete Task", width=10, command=delete_task).pack(side="left", padx=4, pady=4)

# --- PanedWindow (Vertical Layout) ---
paned = tk.PanedWindow(root, orient=tk.VERTICAL)
paned.pack(fill=tk.BOTH, expand=True)

# Top Pane (just placeholder input section if needed)
top_frame = tk.Frame(paned, bg="#f5f5f5", height=100)
tk.Label(top_frame, text="Your Tasks", font=("Arial", 14), bg="#f5f5f5").pack(pady=20)
paned.add(top_frame)

# Bottom Pane (Task List Display)
bottom_frame = tk.Frame(paned)
task_listbox = tk.Listbox(bottom_frame, font=("Arial", 12))
task_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
paned.add(bottom_frame)

root.mainloop()
