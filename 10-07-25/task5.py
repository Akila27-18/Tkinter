import tkinter as tk
import threading
import time

def progress(label):
    for i in range(1, 6):
        time.sleep(1)
        # Safely update the label from the main thread
        label.after(0, lambda i=i: label.config(text=f"Progress: {i}/5"))

def start_progress(label):
    threading.Thread(target=progress, args=(label,), daemon=True).start()

root = tk.Tk()
root.title("Task 05 - Progress per Second")
root.geometry("300x150")

progress_label = tk.Label(root, text="Progress: 0/5", font=("Arial", 20))
progress_label.pack(pady=10)

tk.Button(root, text="Start", command=lambda: start_progress(progress_label)).pack()

root.mainloop()
