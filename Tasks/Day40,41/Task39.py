import tkinter as tk
from tkinter import messagebox
import re

# Function to validate email
def validate_email():
    email = email_entry.get().strip()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not email:
        messagebox.showwarning("Warning", "Email field cannot be empty.")
    elif not re.match(pattern, email):
        messagebox.showwarning("Warning", "Invalid email format.")
    else:
        print("Email is valid:", email)

# Create main window
root = tk.Tk()
root.title("Email Check")
root.geometry("300x150")

# Email entry
tk.Label(root, text="Enter your email:").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Validate button
tk.Button(root, text="Check Email", command=validate_email).pack(pady=10)

# Start the event loop
root.mainloop()
