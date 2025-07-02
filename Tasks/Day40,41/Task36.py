import tkinter as tk
from tkinter import messagebox
import re

# Function to validate email
def validate_email():
    email = email_entry.get().strip()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        print("Valid Email:", email)
    else:
        messagebox.showwarning("Invalid Email", "Please enter a valid email address.")

# Create main window
root = tk.Tk()
root.title("Email Validation")
root.geometry("300x150")

# Email entry
tk.Label(root, text="Enter your email:").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Validate button
validate_btn = tk.Button(root, text="Validate Email", command=validate_email)
validate_btn.pack(pady=10)

# Start the event loop
root.mainloop()
