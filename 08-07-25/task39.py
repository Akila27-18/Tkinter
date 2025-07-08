import tkinter as tk

def new():
    print("New file")

def open_file():
    print("Open file")

def save():
    print("Save file")

def exit_app():
    root.quit()

root = tk.Tk()

toolbar = tk.Frame(root, bg="lightgray")
toolbar.pack(side="top", fill="x")

tk.Button(toolbar, text="New", command=new).pack(side="left")
tk.Button(toolbar, text="Open", command=open_file).pack(side="left")
tk.Button(toolbar, text="Save", command=save).pack(side="left")
tk.Button(toolbar, text="Exit", command=exit_app).pack(side="left")

root.mainloop()
