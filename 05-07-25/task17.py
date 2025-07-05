import tkinter as tk
import re

def validate_email():
    email = email_entry.get().strip()
    # Simple regex for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        result_label.config(text="Valid Email ✅", fg="green")
    else:
        result_label.config(text="Invalid Email ❌", fg="red")

# Main Window
root = tk.Tk()
root.title("Email Validator App")
root.geometry("350x180")

# Email Entry
tk.Label(root, text="Enter Email:", font=("Arial", 10)).pack(pady=10)
email_entry = tk.Entry(root, width=30, font=("Arial", 10))
email_entry.pack()

# Validate Button
validate_button = tk.Button(root, text="Validate Email", command=validate_email)
validate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
