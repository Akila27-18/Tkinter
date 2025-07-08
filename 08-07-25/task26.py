import tkinter as tk

root = tk.Tk()
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
edit_menu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menubar)
root.mainloop()
