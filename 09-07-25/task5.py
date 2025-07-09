# task5_entry_disable_on_click.py
import tkinter as tk

def lock_entry():
    entry.config(state="disabled")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Lock Entry", command=lock_entry).pack()
root.mainloop()
