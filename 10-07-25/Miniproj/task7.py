import tkinter as tk
from tkinter import ttk
import threading
import time

def fetch_data():
    # Disable button to prevent multiple clicks
    fetch_button.config(state=tk.DISABLED)
    result_label.config(text="Fetching...")

    def background_task():
        # Simulate delay (e.g., API call)
        time.sleep(3)
        result = "Data fetched: {'user': 'Alice', 'status': 'Active'}"

        # Use after() to update GUI safely
        root.after(0, update_label, result)

    threading.Thread(target=background_task).start()

def update_label(result):
    result_label.config(text=result)
    fetch_button.config(state=tk.NORMAL)

# GUI setup
root = tk.Tk()
root.title("Background Data Fetcher")
root.geometry("400x200")

ttk.Label(root, text="Click to fetch data from server:").pack(pady=10)

fetch_button = ttk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=5)

result_label = ttk.Label(root, text="", foreground="blue", wraplength=380, justify="center")
result_label.pack(pady=20)

root.mainloop()
