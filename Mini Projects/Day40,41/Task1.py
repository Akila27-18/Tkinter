import tkinter as tk
from tkinter import messagebox
import re
import os

# File to store user data
USER_FILE = "users.txt"

# Validate email using regex
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Save user to file
def save_user(username, email, password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{email},{password}\n")

# Load users from file
def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    users[parts[0]] = (parts[1], parts[2])  # username: (email, password)
    return users

# Register function
def register():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()

    if not username or not email or not password:
        label_status.config(text="All fields are required", fg="red")
        return

    if not is_valid_email(email):
        label_status.config(text="Invalid email format", fg="red")
        return

    users = load_users()
    if username in users:
        label_status.config(text="Username already exists", fg="red")
        return

    save_user(username, email, password)
    label_status.config(text="Registration successful!", fg="green")

# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()
    users = load_users()

    if username in users and users[username][1] == password:
        label_status.config(text="Login successful!", fg="green")
    else:
        label_status.config(text="Invalid username or password", fg="red")

# --- GUI Setup ---
root = tk.Tk()
root.title("Login & Registration")
root.geometry("300x300")

# Username
tk.Label(root, text="Username:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Email (only for registration)
tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Password
tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Status Label
label_status = tk.Label(root, text="", fg="red")
label_status.pack(pady=5)

# Buttons
tk.Button(root, text="Register", command=register).pack(pady=5)
tk.Button(root, text="Login", command=login).pack()

root.mainloop()
