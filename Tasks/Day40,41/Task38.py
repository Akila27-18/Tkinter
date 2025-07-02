import tkinter as tk
from tkinter import messagebox

# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

# Function to check login
def login():
    username = username_entry.get().strip()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("Login Success")
    else:
        messagebox.showwarning("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password label and entry
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

# Login button
login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack(pady=15)

# Start the event loop
root.mainloop()
