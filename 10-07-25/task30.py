import tkinter as tk
import sqlite3

def create_gpa_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gpa_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            subject1 REAL,
            subject2 REAL,
            subject3 REAL,
            gpa REAL
        )
    """)
    conn.commit()
    conn.close()

def calculate_gpa():
    try:
        marks = [float(entry1.get()), float(entry2.get()), float(entry3.get())]
        gpa = round(sum(marks) / 3, 2)
        entry_gpa.delete(0, tk.END)
        entry_gpa.insert(0, str(gpa))

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO gpa_records (name, subject1, subject2, subject3, gpa) VALUES (?, ?, ?, ?, ?)",
                       (entry_name.get(), marks[0], marks[1], marks[2], gpa))
        conn.commit()
        conn.close()
        lbl_status.config(text="GPA Saved!", fg="green")
    except ValueError:
        lbl_status.config(text="Enter valid numbers!", fg="red")

create_gpa_table()

root = tk.Tk()
root.title("GPA Calculator")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Subject 1:").grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

tk.Label(root, text="Subject 2:").grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

tk.Label(root, text="Subject 3:").grid(row=3, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=3, column=1)

tk.Label(root, text="GPA:").grid(row=4, column=0)
entry_gpa = tk.Entry(root)
entry_gpa.grid(row=4, column=1)

tk.Button(root, text="Calculate GPA", command=calculate_gpa).grid(row=5, column=0, columnspan=2, pady=10)

lbl_status = tk.Label(root, text="")
lbl_status.grid(row=6, column=0, columnspan=2)

root.mainloop()
