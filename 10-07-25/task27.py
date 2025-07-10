import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_users_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def login():
    uname = entry_username.get()
    pwd = entry_password.get()
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (uname, pwd))
    result = cursor.fetchone()
    conn.close()
    if result:
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid credentials")

create_users_table()

root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username:").grid(row=0, column=0)
tk.Label(root, text="Password:").grid(row=1, column=0)

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
