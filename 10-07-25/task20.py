import tkinter as tk
import sqlite3

def update_record():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET age=?, grade=? WHERE name=?", 
                   (entry_age.get(), entry_grade.get(), entry_name.get()))
    conn.commit()
    conn.close()
    lbl_status.config(text="Record Updated", fg="green")

def delete_record():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name=?", (entry_name.get(),))
    conn.commit()
    conn.close()
    lbl_status.config(text="Record Deleted", fg="red")

root = tk.Tk()
root.title("Update/Delete Student")

tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Label(root, text="Grade:").grid(row=2, column=0)

entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_grade = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_grade.grid(row=2, column=1)

tk.Button(root, text="Update", command=update_record).grid(row=3, column=0)
tk.Button(root, text="Delete", command=delete_record).grid(row=3, column=1)

lbl_status = tk.Label(root, text="")
lbl_status.grid(row=4, column=0, columnspan=2)

root.mainloop()
