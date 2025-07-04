import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "1234"

# --- Function to validate login
def validate_login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == USERNAME and pwd == PASSWORD:
        root.destroy()  # Close login window
        open_welcome_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# --- Function to open welcome window
def open_welcome_window():
    welcome = tk.Tk()
    welcome.title("Welcome")
    welcome.geometry("400x200")

    label = tk.Label(welcome, text=f"Welcome, {USERNAME}!", font=("Arial", 18))
    label.pack(expand=True)

    welcome.mainloop()

# --- Login window
root = tk.Tk()
root.title("Login")
root.geometry("400x250")

# Center Frame with .place()
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Username:").grid(row=0, column=0, pady=5, sticky='e')
entry_user = tk.Entry(frame, width=25)
entry_user.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Password:").grid(row=1, column=0, pady=5, sticky='e')
entry_pass = tk.Entry(frame, show="*", width=25)
entry_pass.grid(row=1, column=1, pady=5)

btn_login = tk.Button(frame, text="Login", command=validate_login, bg="blue", fg="white", width=20)
btn_login.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()
