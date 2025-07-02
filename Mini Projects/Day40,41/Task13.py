import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re

def calculate_age():
    dob_str = entry_dob.get().strip()
    pattern = r'^\d{4}-\d{2}-\d{2}$'

    if not re.match(pattern, dob_str):
        result_label.config(text="❌ Invalid format (YYYY-MM-DD)", fg="red")
        return

    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"✅ Age: {age} years", fg="green")
    except ValueError:
        result_label.config(text="❌ Invalid date", fg="red")

# --- GUI Setup ---
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

# Widgets
tk.Label(root, text="Enter DOB (YYYY-MM-DD):").pack(pady=10)
entry_dob = tk.Entry(root, width=20)
entry_dob.pack()

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
