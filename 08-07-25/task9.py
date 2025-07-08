import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

sidebar = tk.Frame(root, bg="#ddd", width=100)
sidebar.pack(side="left", fill="y")

tk.Button(sidebar, text="Home").pack(pady=5)
tk.Button(sidebar, text="Profile").pack(pady=5)
tk.Button(sidebar, text="Settings").pack(pady=5)

root.mainloop()
