import tkinter as tk
import threading
import time

def countdown(label):
    for i in range(10, -1, -1):
        time.sleep(1)
        label.after(0, lambda i=i: label.config(text=f"Countdown: {i}"))

def start_countdown(label):
    threading.Thread(target=countdown, args=(label,), daemon=True).start()

root = tk.Tk()
root.title("Task 04 - Countdown Timer")
root.geometry("300x150")

count_label = tk.Label(root, text="Countdown: 10", font=("Arial", 20))
count_label.pack(pady=10)

tk.Button(root, text="Start Countdown", command=lambda: start_countdown(count_label)).pack()

root.mainloop()
