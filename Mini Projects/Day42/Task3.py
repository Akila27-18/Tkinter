import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Entry and Add Button
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        add_btn.pack(pady=2)

        # Frame for Listbox + Scrollbar
        frame = tk.Frame(root)
        frame.pack()

        self.task_listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        scrollbar.config(command=self.task_listbox.yview)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        remove_btn = tk.Button(btn_frame, text="Remove Selected", command=self.remove_task)
        remove_btn.grid(row=0, column=0, padx=5)

        save_btn = tk.Button(btn_frame, text="Save Tasks", command=self.save_tasks)
        save_btn.grid(row=0, column=1, padx=5)

        load_btn = tk.Button(btn_frame, text="Load Tasks", command=self.load_tasks)
        load_btn.grid(row=0, column=2, padx=5)

        # Double-click to mark complete
        self.task_listbox.bind("<Double-Button-1>", self.toggle_complete)

        # Track completed tasks (index: True/False)
        self.completed = {}

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_listbox.delete(index)
            if index in self.completed:
                del self.completed[index]
            # Shift completed state keys down
            self.completed = {
                i - 1 if i > index else i: val
                for i, val in self.completed.items() if i != index
            }

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open("tasks.txt", "w") as f:
            for i, task in enumerate(tasks):
                status = "[X]" if self.completed.get(i) else "[ ]"
                f.write(f"{status} {task}\n")
        messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.completed.clear()
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("[X] "):
                        self.task_listbox.insert(tk.END, line[4:])
                        self.mark_task(len(self.task_listbox.get(0, tk.END)) - 1, True)
                    elif line.startswith("[ ] "):
                        self.task_listbox.insert(tk.END, line[4:])
        except FileNotFoundError:
            messagebox.showwarning("Not Found", "No saved tasks found.")

    def toggle_complete(self, event):
        index = self.task_listbox.curselection()
        if not index:
            return
        index = index[0]
        is_done = self.completed.get(index, False)
        self.mark_task(index, not is_done)

    def mark_task(self, index, complete=True):
        task = self.task_listbox.get(index)
        self.task_listbox.delete(index)
        self.task_listbox.insert(index, task)
        font = ("Arial", 10, "overstrike" if complete else "normal")
        self.task_listbox.itemconfig(index, {'fg': 'gray' if complete else 'black', 'font': font})
        self.completed[index] = complete

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
