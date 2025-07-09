# task28_login_enter_submit.py
import tkinter as tk
from tkinter import messagebox

def submit(event=None):
    messagebox.showinfo("Login", f"Username: {username.get()}")

root = tk.Tk()
username = tk.StringVar()

tk.Entry(root, textvariable=username).pack(pady=5)
tk.Button(root, text="Login", command=submit).pack(pady=5)

root.bind("<Return>", submit)
root.mainloop()
