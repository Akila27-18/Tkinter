import tkinter as tk
from tkinter import messagebox
import re

# Email validation pattern
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Function to add feedback
def add_feedback():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    comment = comment_text.get("1.0", tk.END).strip()

    # Validations
    if not name:
        messagebox.showwarning("Validation Error", "Name is required.")
        return
    if not re.match(EMAIL_REGEX, email):
        messagebox.showwarning("Validation Error", "Invalid email format.")
        return
    if not comment:
        messagebox.showwarning("Validation Error", "Comment cannot be empty.")
        return

    # Add feedback to listbox
    feedback_entry = f"{name} ({email}): {comment}"
    feedback_listbox.insert(tk.END, feedback_entry)

    # Clear inputs
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    comment_text.delete("1.0", tk.END)

# Function to clear all feedbacks
def clear_feedback():
    feedback_listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Feedback Collector")
root.geometry("500x500")

# Name
tk.Label(root, text="Name:").place(x=20, y=20)
name_entry = tk.Entry(root, width=40)
name_entry.place(x=100, y=20)

# Email
tk.Label(root, text="Email:").place(x=20, y=60)
email_entry = tk.Entry(root, width=40)
email_entry.place(x=100, y=60)

# Comment
tk.Label(root, text="Comment:").place(x=20, y=100)
comment_text = tk.Text(root, width=38, height=5)
comment_text.place(x=100, y=100)

# Buttons
add_btn = tk.Button(root, text="Add Feedback", command=add_feedback)
add_btn.place(x=100, y=200)

clear_btn = tk.Button(root, text="Clear All", command=clear_feedback)
clear_btn.place(x=220, y=200)

# Feedback Listbox with Scrollbar
tk.Label(root, text="Feedbacks:").place(x=20, y=250)
frame = tk.Frame(root)
frame.place(x=100, y=250, width=350, height=200)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

feedback_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=50, height=10)
feedback_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=feedback_listbox.yview)

# Run the app
root.mainloop()
