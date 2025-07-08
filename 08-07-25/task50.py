import tkinter as tk
from tkinter import messagebox
import re

def open_email_dialog():
    def validate_email():
        email = email_entry.get()
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            label.config(text=f"Email: {email}")
            dialog.destroy()
        else:
            messagebox.showerror("Invalid", "Enter a valid email address")

    dialog = tk.Toplevel(root)
    dialog.title("Email Entry")

    tk.Label(dialog, text="Enter Email:").pack(padx=10, pady=5)
    email_entry = tk.Entry(dialog)
    email_entry.pack(padx=10, pady=5)
    tk.Button(dialog, text="Submit", command=validate_email).pack(pady=10)

root = tk.Tk()
label = tk.Label(root, text="Your email will appear here")
label.pack(pady=10)

tk.Button(root, text="Enter Email", command=open_email_dialog).pack()
root.mainloop()
