import tkinter as tk
import sqlite3

def view_all():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, grade FROM students")
    records = cursor.fetchall()
    conn.close()
    
    listbox.delete(0, tk.END)
    for record in records:
        listbox.insert(tk.END, f"Name: {record[0]}, Age: {record[1]}, Grade: {record[2]}")

root = tk.Tk()
root.title("View All Students")

tk.Button(root, text="View All", command=view_all).pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

root.mainloop()
