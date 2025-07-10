import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import csv
import os

# Create contacts table
def create_table():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Validate a contact record
def is_valid_contact(name, email, phone):
    return name.strip() != "" and "@" in email and phone.isdigit()

# Import CSV function
def import_csv():
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )
    if not file_path:
        return

    if not os.path.exists(file_path):
        message_label.config(text="File not found.", foreground="red")
        return

    try:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        inserted = 0
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 3:
                    continue  # Skip invalid row
                name, email, phone = row
                if is_valid_contact(name, email, phone):
                    cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
                    inserted += 1
        conn.commit()
        conn.close()
        message_label.config(text=f"Import successful! {inserted} contacts added.", foreground="green")
    except Exception as e:
        message_label.config(text=f"Error: {str(e)}", foreground="red")

# GUI setup
create_table()

root = tk.Tk()
root.title("Contact CSV Importer")
root.geometry("400x200")

ttk.Label(root, text="Import Contacts from CSV to SQLite").pack(pady=10)

ttk.Button(root, text="Select CSV File", command=import_csv).pack(pady=10)

message_label = ttk.Label(root, text="", wraplength=380, justify="center")
message_label.pack(pady=10)

root.mainloop()
