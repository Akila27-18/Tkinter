import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import os

# Create DB and table if not exists
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_record():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    course = entry_course.get().strip()

    if not name or not age or not course:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    if not age.isdigit():
        messagebox.showerror("Validation Error", "Age must be numeric.")
        return

    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, int(age), course))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student registered successfully!")
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)

def view_all():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT name, age, course FROM students")
    rows = c.fetchall()
    conn.close()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"Name: {row[0]} | Age: {row[1]} | Course: {row[2]}")

def export_records():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT name, age, course FROM students")
    rows = c.fetchall()
    conn.close()

    with open(file_path, "w") as f:
        for row in rows:
            f.write(f"Name: {row[0]}, Age: {row[1]}, Course: {row[2]}\n")

    messagebox.showinfo("Exported", f"Records saved to:\n{file_path}")

# UI Setup
root = tk.Tk()
root.title("Student Registration System")
root.geometry("500x450")

tk.Label(root, text="Name:").pack(pady=(10, 0))
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Age:").pack(pady=(10, 0))
entry_age = tk.Entry(root, width=40)
entry_age.pack()

tk.Label(root, text="Course:").pack(pady=(10, 0))
entry_course = tk.Entry(root, width=40)
entry_course.pack()

tk.Button(root, text="Save", width=15, command=save_record).pack(pady=10)
tk.Button(root, text="View All", width=15, command=view_all).pack()
tk.Button(root, text="Export to TXT", width=15, command=export_records).pack(pady=10)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

init_db()
root.mainloop()
