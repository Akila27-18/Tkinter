import tkinter as tk
import sqlite3

def load_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    listbox.delete(0, tk.END)
    for r in rows:
        listbox.insert(tk.END, r[0])

def on_select(event):
    selected_name = listbox.get(listbox.curselection())
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, grade FROM students WHERE name=?", (selected_name,))
    record = cursor.fetchone()
    conn.close()

    if record:
        entry_name.delete(0, tk.END)
        entry_name.insert(0, record[0])
        entry_age.delete(0, tk.END)
        entry_age.insert(0, record[1])
        entry_grade.delete(0, tk.END)
        entry_grade.insert(0, record[2])

root = tk.Tk()
root.title("Edit Selected Student")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Grade:").grid(row=2, column=0)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1)

tk.Button(root, text="Load Names", command=load_students).grid(row=3, column=0, columnspan=2)

listbox = tk.Listbox(root, width=40)
listbox.grid(row=4, column=0, columnspan=2, pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
