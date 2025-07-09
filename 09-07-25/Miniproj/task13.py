import tkinter as tk

class TaskManager(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=10, pady=10)

        # Entry to add new tasks
        self.task_entry = tk.Entry(self, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=5)
        self.task_entry.bind("<Return>", self.add_task)

        # Listbox to show tasks
        self.task_listbox = tk.Listbox(self, width=40, height=10, font=("Arial", 12))
        self.task_listbox.pack(pady=5)
        self.task_listbox.bind("<Double-Button-1>", self.toggle_task)

        # Add Task Button
        add_btn = tk.Button(self, text="Add Task", command=self.add_task)
        add_btn.pack(pady=5)

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def toggle_task(self, event):
        # Get selected index
        index = self.task_listbox.curselection()
        if not index:
            return
        idx = index[0]
        task_text = self.task_listbox.get(idx)

        # Toggle ✔ prefix
        if task_text.startswith("✔ "):
            task_text = task_text[2:]  # remove checkmark
        else:
            task_text = "✔ " + task_text  # add checkmark

        # Update task in listbox
        self.task_listbox.delete(idx)
        self.task_listbox.insert(idx, task_text)

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Task Manager with Completion Toggle")
    root.geometry("400x350")
    app = TaskManager(master=root)
    app.mainloop()
