import tkinter as tk

def dummy(): pass

root = tk.Tk()
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=dummy)
file_menu.add_command(label="Open", command=dummy)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)
root.mainloop()
