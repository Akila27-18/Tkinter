import tkinter as tk
from tkinter import messagebox
import re

def is_valid_name(name):
    return name.isalpha()

def is_valid_email(email):
    # Basic email pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def show_dialog(name, email):
    dialog = tk.Toplevel(root)
    dialog.title("Submission Received")
    dialog.geometry("300x150")
    dialog.resizable(False, False)

    # Message
    tk.Label(dialog, text="Form Submitted Successfully!", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(dialog, text=f"Name: {name}", font=("Arial", 11)).pack()
    tk.Label(dialog, text=f"Email: {email}", font=("Arial", 11)).pack()

    # Close button
    tk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=15)

def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not email:
        messagebox.showwarning("Validation Error", "All fields are required.")
        return

    if not is_valid_name(name):
        messagebox.showwarning("Validation Error", "Name must contain only alphabets.")
        return

    if not is_valid_email(email):
        messagebox.showwarning("Validation Error", "Enter a valid email address.")
        return

    show_dialog(name, email)

# Main window
root = tk.Tk()
root.title("Validated Form Submission")
root.geometry("350x230")

# Labels and Entries
tk.Label(root, text="Name:").pack(pady=(10, 2))
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Email:").pack(pady=(10, 2))
email_entry = tk.Entry(root, width=30)
email_entry.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

root.mainloop()
