# task35_entry_caps_lock.py
import tkinter as tk

def to_upper(event):
    entry.insert("end", event.char.upper())
    return "break"

root = tk.Tk()
entry = tk.Entry(root)
entry.pack(pady=20)
entry.bind("<KeyPress>", to_upper)
root.mainloop()
