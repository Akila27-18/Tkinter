import tkinter as tk

# Preset credentials
USERNAME = "admin"
PASSWORD = "12345"

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        result_label.config(text=f"Welcome, {username}!", fg="green")
    else:
        result_label.config(text="Invalid username or password", fg="red")

# GUI setup
root = tk.Tk()
root.title("Simple Login Form")
root.geometry("300x220")

# Username Label and Entry
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.pack()

# Password Label and Entry
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

# Login Button
tk.Button(root, text="Login", command=login).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
