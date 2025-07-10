
import tkinter as tk
from tkinter import ttk
import threading
import time

def run_progress(bar, label):
    for i in range(101):
        time.sleep(0.05)
        bar.after(0, bar.config, {'value': i})
        label.after(0, label.config, {'text': f"{i}%"})

root = tk.Tk()
root.title("Task 09 - Progress Bar")
root.geometry("300x150")

progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)

percent_label = tk.Label(root, text="0%")
percent_label.pack()

tk.Button(root, text="Start", command=lambda: threading.Thread(target=run_progress, args=(progress, percent_label)).start()).pack()

root.mainloop()
