import tkinter as tk
from tkinter import messagebox
import re

# Email validation regex
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email)

# Name validation: only letters and spaces
def validate_name(name):
    return re.match(r'^[A-Za-z ]+$', name)

# Submit action
def submit_feedback():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    comments = comments_text.get("1.0", tk.END).strip()

    if not name or not email or not comments:
        messagebox.showwarning("Missing Fields", "All fields are required.")
        return

    if not validate_name(name):
        messagebox.showerror("Invalid Name", "Name must contain only letters and spaces.")
        return

    if not validate_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    if len(comments) < 10:
        messagebox.showwarning("Comment Too Short", "Comments must be at least 10 characters.")
        return

    # Add to Listbox
    feedback_summary = f"{name} ({email}): {comments[:40]}..."
    feedback_listbox.insert(tk.END, feedback_summary)

    # Clear inputs
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    comments_text.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Feedback Collector")
root.geometry("500x400")
root.resizable(False, False)

# Name
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Email
tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Comments
tk.Label(root, text="Comments:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
comments_text = tk.Text(root, width=30, height=5)
comments_text.grid(row=2, column=1, padx=5, pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_btn.grid(row=3, column=1, pady=10)

# Feedback listbox with scrollbar
tk.Label(root, text="Feedback Summary:").grid(row=4, column=0, columnspan=2, pady=(10, 0))

frame = tk.Frame(root)
frame.grid(row=5, column=0, columnspan=2, padx=10)

scrollbar = tk.Scrollbar(frame)
feedback_listbox = tk.Listbox(frame, width=65, height=8, yscrollcommand=scrollbar.set)
scrollbar.config(command=feedback_listbox.yview)

feedback_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
