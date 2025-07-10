import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_feedback_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            rating INTEGER,
            comment TEXT
        )
    """)
    conn.commit()
    conn.close()

def submit_feedback():
    name = entry_name.get()
    try:
        rating = int(entry_rating.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for rating!")
        return
    comment = entry_comment.get("1.0", tk.END).strip()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (name, rating, comment) VALUES (?, ?, ?)", (name, rating, comment))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Feedback submitted!")

create_feedback_table()

root = tk.Tk()
root.title("Submit Feedback")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Rating (1–5):").grid(row=1, column=0)
entry_rating = tk.Entry(root)
entry_rating.grid(row=1, column=1)

tk.Label(root, text="Comment:").grid(row=2, column=0)
entry_comment = tk.Text(root, height=4, width=30)
entry_comment.grid(row=2, column=1)

tk.Button(root, text="Submit", command=submit_feedback).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
