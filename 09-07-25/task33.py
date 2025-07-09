# task33_ctrls_save.py
import tkinter as tk
from tkinter import messagebox

def save(event):
    messagebox.showinfo("Save", "Simulated Save Triggered (Ctrl+S)")

root = tk.Tk()
root.bind("<Control-s>", save)
tk.Label(root, text="Press Ctrl+S to Save").pack(pady=20)
root.mainloop()
