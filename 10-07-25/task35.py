import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import csv

def import_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [(row['name'], int(row['age']), row['grade']) for row in reader]
        
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "CSV data imported!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to import: {e}")

root = tk.Tk()
root.title("Import CSV")

tk.Button(root, text="Import from CSV", command=import_csv).pack(padx=20, pady=20)

root.mainloop()
