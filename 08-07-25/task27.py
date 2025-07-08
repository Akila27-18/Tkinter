import tkinter as tk

def open_file():
    print("Open clicked")

root = tk.Tk()
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)

menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)
root.mainloop()
