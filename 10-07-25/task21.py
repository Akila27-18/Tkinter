import tkinter as tk
from tkinter import ttk
import sqlite3

def load_names():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM students")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    combo_names['values'] = names

def populate_fields(event):
    name = combo_names.get()
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT age, grade FROM students WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        entry_age.delete(0, tk.END)
        entry_grade.delete(0, tk.END)
        entry_age.insert(0, result[0])
        entry_grade.insert(0, result[1])

root = tk.Tk()
root.title("Select Student by Name")

tk.Label(root, text="Select Name:").grid(row=0, column=0)
combo_names = ttk.Combobox(root, state="readonly")
combo_names.grid(row=0, column=1)
combo_names.bind("<<ComboboxSelected>>", populate_fields)

tk.Label(root, text="Age:").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Grade:").grid(row=2, column=0)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1)

tk.Button(root, text="Load Names", command=load_names).grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
