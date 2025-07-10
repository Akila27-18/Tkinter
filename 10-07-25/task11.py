import tkinter as tk
import threading
import time

def wrong_way(label):
    label.config(text="This will freeze UI...")
    time.sleep(5)  # Blocks main thread
    label.config(text="Done")

def correct_way(label):
    def work():
        time.sleep(5)
        # Safely update GUI from the main thread
        label.after(0, lambda: label.config(text="Done Safely"))
    threading.Thread(target=work, daemon=True).start()

root = tk.Tk()
root.title("Task 11 - Freeze vs after()")
root.geometry("300x200")

status = tk.Label(root, text="Ready", font=("Arial", 14))
status.pack(pady=10)

tk.Button(root, text="Freeze UI", command=lambda: wrong_way(status)).pack(pady=5)
tk.Button(root, text="Safe Update", command=lambda: correct_way(status)).pack(pady=5)

root.mainloop()
