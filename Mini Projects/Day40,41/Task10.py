import tkinter as tk
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def check_email():
    email = entry_email.get().strip()
    if is_valid_email(email):
        result_label.config(text="✅ Valid Email", fg="green")
    else:
        result_label.config(text="❌ Invalid Email", fg="red")

def clear():
    entry_email.delete(0, tk.END)
    result_label.config(text="")

# --- GUI Setup ---
root = tk.Tk()
root.title("Email Validator")
root.geometry("300x200")

# Widgets
tk.Label(root, text="Enter Email:").pack(pady=10)
entry_email = tk.Entry(root, width=30)
entry_email.pack()

tk.Button(root, text="Check", command=check_email).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
