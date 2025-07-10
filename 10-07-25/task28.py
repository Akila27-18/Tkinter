import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_users_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def register():
    uname = entry_username.get()
    pwd = entry_password.get()
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (uname, pwd))
        conn.commit()
        conn.close()
        messagebox.showinfo("Register", "Registration Successful")
    except sqlite3.IntegrityError:
        messagebox.showerror("Register", "Username already exists")

create_users_table()

root = tk.Tk()
root.title("Register User")

tk.Label(root, text="Username:").grid(row=0, column=0)
tk.Label(root, text="Password:").grid(row=1, column=0)

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

tk.Button(root, text="Register", command=register).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
