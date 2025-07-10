import tkinter as tk
from tkinter import messagebox
import threading
import time

def start_task():
    if task_running[0]:
        messagebox.showinfo("Info", "Task is already running.")
        return

    task_running[0] = True
    label_status.config(text="Starting task...")
    threading.Thread(target=run_task, daemon=True).start()

def run_task():
    for i in range(1, 6):
        time.sleep(1)  # Simulate long process
        root.after(0, update_status, f"Processing {i * 20}%...")

    root.after(0, finish_task)

def update_status(msg):
    label_status.config(text=msg)

def finish_task():
    task_running[0] = False
    label_status.config(text="✅ Task completed!")

# GUI Setup
root = tk.Tk()
root.title("Background Task Notifier")
root.geometry("350x200")

tk.Button(root, text="Start Task", font=("Arial", 12), command=start_task).pack(pady=20)
label_status = tk.Label(root, text="Idle", font=("Arial", 12), fg="blue")
label_status.pack()

task_running = [False]  # Mutable flag to track status

root.mainloop()
