import tkinter as tk
from tkinter import ttk
from datetime import datetime

def issue_book():
    user = entry_user.get().strip()
    book = combo_book.get()
    day = spin_day.get()

    # --- Validation ---
    if not user:
        tk.messagebox.showerror("Input Error", "User name cannot be empty.")
        return
    if not book:
        tk.messagebox.showerror("Input Error", "Please select a book.")
        return

    record = f"{user} | {book} | Date: {day}"
    listbox.insert(tk.END, record)
    entry_user.delete(0, tk.END)
    combo_book.set("")
    spin_day.delete(0, tk.END)
    spin_day.insert(0, datetime.now().day)

# --- Main Window ---
root = tk.Tk()
root.title("Library Book Issue System")
root.geometry("400x300")

# --- Labels & Inputs ---
tk.Label(root, text="User Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Book Title:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
combo_book = ttk.Combobox(root, values=[
    "The Great Gatsby", "1984", "To Kill a Mockingbird", 
    "The Catcher in the Rye", "Pride and Prejudice"
], state="readonly")
combo_book.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Issue Day:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
spin_day = tk.Spinbox(root, from_=1, to=31, width=5)
spin_day.grid(row=2, column=1, sticky="w", padx=10, pady=5)
spin_day.delete(0, tk.END)
spin_day.insert(0, datetime.now().day)

# --- Issue Button ---
issue_btn = tk.Button(root, text="Issue Book", command=issue_book)
issue_btn.grid(row=3, column=0, columnspan=2, pady=10)

# --- Listbox with Scrollbar ---
tk.Label(root, text="Issued Records:").grid(row=4, column=0, padx=10, sticky="ne")

frame_listbox = tk.Frame(root)
frame_listbox.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")

listbox = tk.Listbox(frame_listbox, height=8, width=40)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# --- Run ---
root.mainloop()
