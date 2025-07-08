import tkinter as tk
from tkinter import messagebox

def show_warning():
    messagebox.showwarning("Warning", "This action might be unsafe!")

root = tk.Tk()
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=20)
root.mainloop()
