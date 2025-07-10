import tkinter as tk
import threading
import time
import random

def simulate_api_call(label):
    time.sleep(3)
    data = f"Data #{random.randint(100, 999)}"
    # Safe GUI update using lambda
    label.after(0, lambda: label.config(text=f"Fetched: {data}"))

def start_fetch(label):
    threading.Thread(target=simulate_api_call, args=(label,), daemon=True).start()

root = tk.Tk()
root.title("Task 08 - API Fetch Sim")
root.geometry("300x150")

data_label = tk.Label(root, text="No data", font=("Arial", 16))
data_label.pack(pady=10)

tk.Button(root, text="Fetch Data", command=lambda: start_fetch(data_label)).pack()

root.mainloop()
