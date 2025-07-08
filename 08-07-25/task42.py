import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
tk.Label(root, text="Try closing the window").pack(pady=20)
root.mainloop()
