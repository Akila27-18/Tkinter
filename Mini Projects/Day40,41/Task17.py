import tkinter as tk
from tkinter import messagebox
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def submit_feedback():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    feedback = text_feedback.get("1.0", tk.END).strip()

    if not name or not email or not feedback:
        messagebox.showwarning("Validation Error", "All fields are required.")
        return
    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    with open("feedback.txt", "a") as f:
        f.write(f"Name: {name}\nEmail: {email}\nFeedback:\n{feedback}\n{'-'*40}\n")

    messagebox.showinfo("Thank You", "Thank you for your feedback!")

    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_feedback.delete("1.0", tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Feedback Collector")
root.geometry("400x350")

# Labels and Entry/Text widgets
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Feedback:").grid(row=2, column=0, sticky="ne", padx=10, pady=5)
text_feedback = tk.Text(root, width=30, height=10)
text_feedback.grid(row=2, column=1)

# Submit Button
tk.Button(root, text="Submit", command=submit_feedback).grid(row=3, columnspan=2, pady=10)

root.mainloop()
