
import tkinter as tk
import threading
import time
import random

def independent_task(label):
    sleep_time = random.randint(1, 4)
    label.config(text=f"Running {sleep_time}s...")
    time.sleep(sleep_time)
    label.after(0, label.config, {'text': f"Done {sleep_time}s"})

root = tk.Tk()
root.title("Task 15 - Multiple Threads")
root.geometry("300x200")

for i in range(3):
    lbl = tk.Label(root, text=f"Task {i+1}")
    lbl.pack(pady=5)
    tk.Button(root, text=f"Start {i+1}", command=lambda l=lbl: threading.Thread(target=independent_task, args=(l,)).start()).pack()

root.mainloop()
