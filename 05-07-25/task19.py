import tkinter as tk
from tkinter import messagebox

books = []  # Global list to store all book titles

def add_book():
    book = book_entry.get().strip()
    if not book:
        messagebox.showwarning("Input Error", "Book name cannot be empty.")
        return
    books.append(book)
    update_listbox()
    book_entry.delete(0, tk.END)

def remove_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Select Book", "Please select a book to remove.")
        return
    title = listbox.get(selected[0])
    books.remove(title)
    update_listbox()

def update_listbox(filtered=None):
    listbox.delete(0, tk.END)
    for book in (filtered if filtered is not None else books):
        listbox.insert(tk.END, book)

def search_books(event):
    query = search_entry.get().strip().lower()
    filtered = [b for b in books if query in b.lower()]
    update_listbox(filtered)

# GUI Setup
root = tk.Tk()
root.title("Library Book Manager")
root.geometry("500x600")
root.resizable(False, False)

# Book Entry
tk.Label(root, text="Book Name:").pack(anchor="w", padx=10, pady=(10, 0))
book_entry = tk.Entry(root, width=40)
book_entry.pack(padx=10, pady=5)

add_btn = tk.Button(root, text="Add Book", command=add_book)
add_btn.pack(pady=5)

# Search Entry
tk.Label(root, text="Search Book:").pack(anchor="w", padx=10, pady=(10, 0))
search_entry = tk.Entry(root, width=40)
search_entry.pack(padx=10, pady=5)
search_entry.bind("<KeyRelease>", search_books)

# Listbox with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
listbox = tk.Listbox(frame, width=50, height=12, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Remove Button
remove_btn = tk.Button(root, text="Remove Selected Book", command=remove_book)
remove_btn.pack(pady=10)

root.mainloop()
