import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Information", "This is an informational message.")

root = tk.Tk()
tk.Button(root, text="Show Info", command=show_info).pack(pady=20)
root.mainloop()
