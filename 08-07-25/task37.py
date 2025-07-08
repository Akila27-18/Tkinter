import tkinter as tk

def open_file():
    print("Open clicked")

def save_file():
    print("Save clicked")

root = tk.Tk()

toolbar = tk.Frame(root, bg="lightgray")
toolbar.pack(side="top", fill="x")

tk.Button(toolbar, text="Open", command=open_file).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Save", command=save_file).pack(side="left", padx=2, pady=2)

root.mainloop()
