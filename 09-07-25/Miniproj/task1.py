import tkinter as tk
from tkinter import messagebox

def check_fields(event=None):
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if username and password:
        login_btn.config(state="normal")
    else:
        login_btn.config(state="disabled")

def validate_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    if len(username) < 3:
        messagebox.showerror("Invalid Username", "Username must be at least 3 characters long.")
        return
    if len(password) < 6:
        messagebox.showerror("Invalid Password", "Password must be at least 6 characters long.")
        return
    
    # If validations pass
    messagebox.showinfo("Login Success", f"Welcome, {username}!")

# Main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")
root.resizable(False, False)

# Username
tk.Label(root, text="Username:").pack(pady=(15, 5))
username_entry = tk.Entry(root)
username_entry.pack()
username_entry.bind("<KeyRelease>", check_fields)

# Password
tk.Label(root, text="Password:").pack(pady=(10, 5))
password_entry = tk.Entry(root, show="*")
password_entry.pack()
password_entry.bind("<KeyRelease>", check_fields)

# Login Button (initially disabled)
login_btn = tk.Button(root, text="Login", state="disabled", command=validate_login)
login_btn.pack(pady=20)

root.mainloop()
