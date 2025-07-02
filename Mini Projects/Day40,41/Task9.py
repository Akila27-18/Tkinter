import tkinter as tk
from tkinter import messagebox
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def submit_form():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    email = entry_email.get().strip()
    course = entry_course.get().strip()

    # Validation
    if not name or not age or not email or not course:
        messagebox.showerror("Validation Error", "All fields are required.")
        return
    if not age.isdigit() or not (3 < int(age) < 100):
        messagebox.showerror("Validation Error", "Enter a valid age (4–99).")
        return
    if not is_valid_email(email):
        messagebox.showerror("Validation Error", "Invalid email format.")
        return

    # Save to file
    with open("students.txt", "a") as f:
        f.write(f"{name}, {age}, {email}, {course}\n")

    # Show summary
    messagebox.showinfo("Registration Successful",
        f"Student Registered:\n\nName: {name}\nAge: {age}\nEmail: {email}\nCourse: {course}")

    # Clear entries
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_course.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x250")

# Labels and Entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_age = tk.Entry(root, width=30)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=2, column=1)

tk.Label(root, text="Course:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_course = tk.Entry(root, width=30)
entry_course.grid(row=3, column=1)

# Submit button
tk.Button(root, text="Submit", width=20, command=submit_form).grid(row=4, columnspan=2, pady=20)

root.mainloop()
