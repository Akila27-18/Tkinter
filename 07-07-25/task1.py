import tkinter as tk
from tkinter import messagebox
import re

# Sample credentials store (in real apps, use a database)
users = {}

# Email regex pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'


def validate_email(email):
    return re.match(email_pattern, email)


def register_user():
    username = reg_username_entry.get().strip()
    email = reg_email_entry.get().strip()
    password = reg_password_entry.get().strip()

    if not username or not email or not password:
        reg_status.config(text="All fields are required", fg="red")
    elif not validate_email(email):
        reg_status.config(text="Invalid email format", fg="red")
    elif username in users:
        reg_status.config(text="User already exists", fg="red")
    else:
        users[username] = {"email": email, "password": password}
        reg_status.config(text="Registration successful!", fg="green")
        clear_registration()


def login_user():
    username = login_username_entry.get().strip()
    password = login_password_entry.get().strip()

    if not username or not password:
        login_status.config(text="Both fields required", fg="red")
    elif username not in users:
        login_status.config(text="User not found", fg="red")
    elif users[username]["password"] != password:
        login_status.config(text="Incorrect password", fg="red")
    else:
        login_status.config(text=f"Welcome, {username}!", fg="green")
        clear_login()


def clear_registration():
    reg_username_entry.delete(0, tk.END)
    reg_email_entry.delete(0, tk.END)
    reg_password_entry.delete(0, tk.END)


def clear_login():
    login_username_entry.delete(0, tk.END)
    login_password_entry.delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("User Registration & Login System")
root.geometry("500x350")

# ============ Registration Frame ============
reg_frame = tk.LabelFrame(root, text="Register", padx=10, pady=10)
reg_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

tk.Label(reg_frame, text="Username").grid(row=0, column=0, sticky="e")
reg_username_entry = tk.Entry(reg_frame)
reg_username_entry.grid(row=0, column=1)

tk.Label(reg_frame, text="Email").grid(row=1, column=0, sticky="e")
reg_email_entry = tk.Entry(reg_frame)
reg_email_entry.grid(row=1, column=1)

tk.Label(reg_frame, text="Password").grid(row=2, column=0, sticky="e")
reg_password_entry = tk.Entry(reg_frame, show="*")
reg_password_entry.grid(row=2, column=1)

tk.Button(reg_frame, text="Register", command=register_user).grid(row=3, columnspan=2, pady=5)
reg_status = tk.Label(reg_frame, text="", fg="green")
reg_status.grid(row=4, columnspan=2)

# ============ Login Frame ============
login_frame = tk.LabelFrame(root, text="Login", padx=10, pady=10)
login_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

tk.Label(login_frame, text="Username").grid(row=0, column=0, sticky="e")
login_username_entry = tk.Entry(login_frame)
login_username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password").grid(row=1, column=0, sticky="e")
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.grid(row=1, column=1)

tk.Button(login_frame, text="Login", command=login_user).grid(row=2, columnspan=2, pady=5)
login_status = tk.Label(login_frame, text="", fg="green")
login_status.grid(row=3, columnspan=2)

root.mainloop()
