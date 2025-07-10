import tkinter as tk
from tkinter import messagebox
import sqlite3
import time

# Database setup
def setup_database():
    conn = sqlite3.connect("task_timer.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration INTEGER
        )
    """)
    conn.commit()
    conn.close()

# Timer Task Class
class Task:
    def __init__(self, parent, name, summary_callback):
        self.parent = parent
        self.name = name
        self.duration = 0
        self.running = False
        self.timer_id = None
        self.summary_callback = summary_callback

        self.frame = tk.Frame(parent)
        self.label = tk.Label(self.frame, text=name, width=20)
        self.time_label = tk.Label(self.frame, text="00:00:00", width=10)
        self.btn = tk.Button(self.frame, text="Start", command=self.toggle)

        self.label.pack(side=tk.LEFT)
        self.time_label.pack(side=tk.LEFT, padx=10)
        self.btn.pack(side=tk.LEFT)
        self.frame.pack(pady=5)

    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def start(self):
        self.running = True
        self.btn.config(text="Stop")
        self.update_timer()

    def stop(self):
        self.running = False
        if self.timer_id:
            self.parent.after_cancel(self.timer_id)
        self.btn.config(text="Start")
        self.save_to_db()
        self.summary_callback()

    def update_timer(self):
        if self.running:
            self.duration += 1
            self.time_label.config(text=self.format_time(self.duration))
            self.timer_id = self.parent.after(1000, self.update_timer)

    def format_time(self, secs):
        return time.strftime('%H:%M:%S', time.gmtime(secs))

    def save_to_db(self):
        conn = sqlite3.connect("task_timer.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (name, duration) VALUES (?, ?)", (self.name, self.duration))
        conn.commit()
        conn.close()

# Main App
class TaskTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Timer Tracker")

        self.tasks = []

        self.task_name_entry = tk.Entry(root, width=30)
        self.task_name_entry.pack(pady=5)

        self.add_task_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(pady=5)

        self.task_container = tk.Frame(root)
        self.task_container.pack(pady=10)

        self.summary_btn = tk.Button(root, text="View Summary", command=self.view_summary)
        self.summary_btn.pack(pady=5)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

    def add_task(self):
        name = self.task_name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Task name cannot be empty.")
            return

        task = Task(self.task_container, name, self.view_summary)
        self.tasks.append(task)
        self.task_name_entry.delete(0, tk.END)

    def view_summary(self):
        self.listbox.delete(0, tk.END)
        conn = sqlite3.connect("task_timer.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, SUM(duration) FROM tasks GROUP BY name")
        rows = cursor.fetchall()
        conn.close()

        for name, total_sec in rows:
            time_str = time.strftime('%H:%M:%S', time.gmtime(total_sec))
            self.listbox.insert(tk.END, f"{name} - {time_str}")

# Run app
if __name__ == "__main__":
    setup_database()
    root = tk.Tk()
    app = TaskTimerApp(root)
    root.mainloop()
