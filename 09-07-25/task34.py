# task34_f1_help.py
import tkinter as tk
from tkinter import messagebox

def show_help(event):
    messagebox.showinfo("Help", "This is the help dialog.")

root = tk.Tk()
root.bind("<F1>", show_help)
tk.Label(root, text="Press F1 for help").pack(pady=20)
root.mainloop()
