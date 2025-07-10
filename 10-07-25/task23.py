import tkinter as tk
import sqlite3

def show_total():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    conn.close()
    lbl_count.config(text=f"Total Students: {count}")

root = tk.Tk()
root.title("Total Student Count")

tk.Button(root, text="Show Total Students", command=show_total).pack(pady=10)

lbl_count = tk.Label(root, text="Total Students: ")
lbl_count.pack()

root.mainloop()
