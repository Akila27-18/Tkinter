import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3

def export_to_txt():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, grade FROM students")
    rows = cursor.fetchall()
    conn.close()

    with open(file_path, 'w') as f:
        for row in rows:
            f.write(f"Name: {row[0]}, Age: {row[1]}, Grade: {row[2]}\n")
    messagebox.showinfo("Success", "Data exported successfully.")

root = tk.Tk()
root.title("Export Records")

tk.Button(root, text="Export to .txt", command=export_to_txt).pack(padx=20, pady=20)

root.mainloop()
