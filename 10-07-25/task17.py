import tkinter as tk
import sqlite3

def save_record():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                   (entry_name.get(), entry_age.get(), entry_grade.get()))
    conn.commit()
    conn.close()
    lbl_status.config(text="Record Saved!", fg="green")

root = tk.Tk()
root.title("Insert Student Record")

tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Label(root, text="Grade:").grid(row=2, column=0)

entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_grade = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_grade.grid(row=2, column=1)

tk.Button(root, text="Save", command=save_record).grid(row=3, column=0, columnspan=2, pady=5)

lbl_status = tk.Label(root, text="")
lbl_status.grid(row=4, column=0, columnspan=2)

root.mainloop()
