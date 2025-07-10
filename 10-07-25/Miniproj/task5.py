import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

def init_db():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def validate_inputs(name, email, phone):
    if not name or not email or not phone:
        messagebox.showwarning("Validation", "All fields are required.")
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Validation", "Invalid email format.")
        return False
    if not phone.isdigit() or len(phone) < 7:
        messagebox.showerror("Validation", "Phone must be numeric and at least 7 digits.")
        return False
    return True

def add_contact():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()

    if not validate_inputs(name, email, phone):
        return

    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Contact added!")
    clear_fields()
    view_all()

def view_all():
    listbox.delete(0, tk.END)
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("SELECT id, name, email, phone FROM contacts")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

def delete_contact():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Select", "Select a contact to delete.")
        return

    result = messagebox.askyesno("Confirm", "Are you sure you want to delete this contact?")
    if not result:
        return

    contact_id = listbox.get(selection[0]).split("|")[0].strip()
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Deleted", "Contact deleted.")
    view_all()

def search_contact():
    keyword = entry_search.get().strip()
    listbox.delete(0, tk.END)
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("""
        SELECT id, name, email, phone FROM contacts
        WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?
    """, (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    rows = c.fetchall()
    conn.close()
    for row in rows:
        listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("SQLite Address Book")
root.geometry("600x500")

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)

tk.Label(root, text="Search:").pack()
entry_search = tk.Entry(root, width=40)
entry_search.pack()

tk.Button(root, text="Search", command=search_contact).pack()
tk.Button(root, text="View All", command=view_all).pack()
tk.Button(root, text="Delete Selected", command=delete_contact).pack(pady=5)

listbox = tk.Listbox(root, width=80, height=10)
listbox.pack(pady=10)

init_db()
view_all()
root.mainloop()
