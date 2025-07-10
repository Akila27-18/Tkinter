import tkinter as tk
import sqlite3

def load_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, grade FROM students")
    rows = cursor.fetchall()
    conn.close()

    listbox.delete(0, tk.END)
    for r in rows:
        listbox.insert(tk.END, f"{r[0]} | Age: {r[1]} | Grade: {r[2]}")

root = tk.Tk()
root.title("Student List (Scrollable)")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, height=10, width=50, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

tk.Button(root, text="Load Students", command=load_students).pack(pady=5)

root.mainloop()
