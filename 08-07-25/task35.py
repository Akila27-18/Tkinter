import tkinter as tk

def add_recent_file(file_name):
    recent_menu.add_command(label=file_name)

root = tk.Tk()
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
recent_menu = tk.Menu(file_menu, tearoff=0)

file_menu.add_cascade(label="Recent Files", menu=recent_menu)
file_menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Simulate dynamic update
root.after(2000, lambda: add_recent_file("report.docx"))
root.after(4000, lambda: add_recent_file("notes.txt"))

root.mainloop()
