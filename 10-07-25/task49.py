import tkinter as tk
import sqlite3
import os

def create_table():
    conn = sqlite3.connect("filetracker.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS recent_file (id INTEGER PRIMARY KEY, path TEXT)")
    conn.commit()
    conn.close()

def save_path(path):
    conn = sqlite3.connect("filetracker.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM recent_file")
    cursor.execute("INSERT INTO recent_file (path) VALUES (?)", (path,))
    conn.commit()
    conn.close()

def load_recent():
    conn = sqlite3.connect("filetracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT path FROM recent_file ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    if result and os.path.exists(result[0]):
        with open(result[0], "r") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())
        lbl_status.config(text=f"Loaded: {result[0]}")
    else:
        lbl_status.config(text="No recent file found.")

def open_file():
    from tkinter import filedialog
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "r") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())
        save_path(path)
        lbl_status.config(text=f"Opened: {path}")

create_table()

root = tk.Tk()
root.title("Auto-Load Recent File")

tk.Button(root, text="Open File", command=open_file).pack()
tk.Button(root, text="Load Recent", command=load_recent).pack()

text = tk.Text(root, width=60, height=20)
text.pack()

lbl_status = tk.Label(root, text="")
lbl_status.pack()

load_recent()

root.mainloop()
