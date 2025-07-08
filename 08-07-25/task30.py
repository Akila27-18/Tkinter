import tkinter as tk
from tkinter import messagebox

def show_about():
    messagebox.showinfo("About", "This is a sample application.")

root = tk.Tk()
menubar = tk.Menu(root)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about)

menubar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menubar)
root.mainloop()
