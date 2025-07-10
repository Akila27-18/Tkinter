import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def add_email():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    
    if not name or not email:
        messagebox.showwarning("Input Error", "Please enter both name and email.")
        return
    
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        messagebox.showwarning("Input Error", "Invalid email format.")
        return
    
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO emails (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Email added successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists!")

create_table()

root = tk.Tk()
root.title("Add Email")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_name = tk.Entry(root, width=30)
entry_email = tk.Entry(root, width=30)

entry_name.grid(row=0, column=1, pady=5)
entry_email.grid(row=1, column=1, pady=5)

tk.Button(root, text="Add Email", command=add_email).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
