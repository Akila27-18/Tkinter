import tkinter as tk

def open_file(event=None):
    print("Ctrl+O pressed - Open File")

root = tk.Tk()
root.bind('<Control-o>', open_file)

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")

menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)
root.mainloop()
