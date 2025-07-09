# task11_reset_widgets.py
import tkinter as tk

def reset_all():
    entry.config(state="normal")
    btn.config(state="normal")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
btn = tk.Button(root, text="Click Me", command=lambda: btn.config(state="disabled"))
btn.pack()
tk.Button(root, text="Reset", command=reset_all).pack()
root.mainloop()
