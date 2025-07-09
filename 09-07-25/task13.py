# task13_disable_spinbox.py
import tkinter as tk

def toggle_spin():
    spin.config(state="disabled" if var.get() else "normal")

root = tk.Tk()
var = tk.BooleanVar()
tk.Checkbutton(root, text="Disable Spinbox", variable=var, command=toggle_spin).pack()
spin = tk.Spinbox(root, from_=0, to=10)
spin.pack()
root.mainloop()
