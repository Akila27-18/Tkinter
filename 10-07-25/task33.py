import tkinter as tk
from tkinter import messagebox
import sqlite3

def delete_record():
    name = entry_name.get()
    if messagebox.askyesno("Confirm", f"Delete record for '{name}'?"):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE name=?", (name,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Record deleted.")
    else:
        messagebox.showinfo("Cancelled", "Deletion cancelled.")

root = tk.Tk()
root.title("Delete with Confirmation")

tk.Label(root, text="Enter Name to Delete:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Button(root, text="Delete", command=delete_record).pack(pady=10)

root.mainloop()
