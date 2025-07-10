import tkinter as tk
import sqlite3

def search_student():
    name_part = entry_search.get()
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, grade FROM students WHERE name LIKE ?", ('%' + name_part + '%',))
    results = cursor.fetchall()
    conn.close()
    
    listbox.delete(0, tk.END)
    for r in results:
        listbox.insert(tk.END, f"{r[0]}, Age: {r[1]}, Grade: {r[2]}")

root = tk.Tk()
root.title("Search Student")

tk.Label(root, text="Enter name to search:").pack()
entry_search = tk.Entry(root)
entry_search.pack()

tk.Button(root, text="Search", command=search_student).pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

root.mainloop()
