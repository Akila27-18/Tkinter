import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------- DATABASE SETUP ----------
def create_table():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ---------- FUNCTIONS ----------
def refresh_list():
    listbox.delete(0, tk.END)
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, author, title, year FROM books")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]}: {row[1]} - '{row[2]}' ({row[3]})")
    conn.close()

def add_book():
    author = entry_author.get().strip()
    title = entry_title.get().strip()
    year = entry_year.get().strip()

    if not author or not title or not year.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter valid book details.")
        return

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (author, title, year) VALUES (?, ?, ?)", (author, title, int(year)))
    conn.commit()
    conn.close()
    refresh_list()
    clear_fields()

def delete_book():
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    book_id = int(listbox.get(index).split(":")[0])

    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this book?"):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        refresh_list()

def edit_book():
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    global current_edit_id
    current_edit_id = int(listbox.get(index).split(":")[0])

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT author, title, year FROM books WHERE id = ?", (current_edit_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        entry_author.delete(0, tk.END)
        entry_author.insert(0, row[0])
        entry_title.delete(0, tk.END)
        entry_title.insert(0, row[1])
        entry_year.delete(0, tk.END)
        entry_year.insert(0, row[2])
        btn_add.config(state=tk.DISABLED)
        btn_update.config(state=tk.NORMAL)

def update_book():
    if current_edit_id is None:
        return

    author = entry_author.get().strip()
    title = entry_title.get().strip()
    year = entry_year.get().strip()

    if not author or not title or not year.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter valid book details.")
        return

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET author = ?, title = ?, year = ? WHERE id = ?",
                   (author, title, int(year), current_edit_id))
    conn.commit()
    conn.close()
    refresh_list()
    clear_fields()
    btn_add.config(state=tk.NORMAL)
    btn_update.config(state=tk.DISABLED)

def clear_fields():
    entry_author.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    global current_edit_id
    current_edit_id = None
    btn_add.config(state=tk.NORMAL)
    btn_update.config(state=tk.DISABLED)

# ---------- GUI SETUP ----------
create_table()
current_edit_id = None

root = tk.Tk()
root.title("Book Library Manager")
root.geometry("500x400")

# Input fields
frame_form = ttk.Frame(root)
frame_form.pack(pady=10)

ttk.Label(frame_form, text="Author:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_author = ttk.Entry(frame_form, width=30)
entry_author.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Title:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_title = ttk.Entry(frame_form, width=30)
entry_title.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Year:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_year = ttk.Entry(frame_form, width=30)
entry_year.grid(row=2, column=1, padx=5, pady=5)

# Buttons
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=10)

btn_add = ttk.Button(frame_buttons, text="Add Book", command=add_book)
btn_add.grid(row=0, column=0, padx=5)

btn_update = ttk.Button(frame_buttons, text="Update Book", command=update_book, state=tk.DISABLED)
btn_update.grid(row=0, column=1, padx=5)

btn_edit = ttk.Button(frame_buttons, text="Edit Selected", command=edit_book)
btn_edit.grid(row=0, column=2, padx=5)

btn_delete = ttk.Button(frame_buttons, text="Delete Selected", command=delete_book)
btn_delete.grid(row=0, column=3, padx=5)

# Listbox
listbox = tk.Listbox(root, width=70, height=10)
listbox.pack(pady=10)

refresh_list()

root.mainloop()
