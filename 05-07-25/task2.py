import tkinter as tk
from tkinter import messagebox

# Sample credentials for validation
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Field validation
    if not username and not password:
        messagebox.showwarning("Validation Error", "Please enter both username and password.")
        return
    elif not username:
        messagebox.showwarning("Validation Error", "Username cannot be empty.")
        return
    elif not password:
        messagebox.showwarning("Validation Error", "Password cannot be empty.")
        return

    # Credential check
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        open_welcome_window(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_welcome_window(username):
    welcome_window = tk.Toplevel(root)
    welcome_window.title("Welcome")
    welcome_window.geometry("300x150")

    welcome_label = tk.Label(welcome_window, text=f"Welcome, {username}!", font=("Arial", 14))
    welcome_label.pack(expand=True, pady=30)

# Main Window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Username
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

# Password
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

root.mainloop()
