import tkinter as tk

root = tk.Tk()

toolbar = tk.Frame(root, bg="lightgray")
toolbar.pack(side="top", fill="x")

for name in ["New", "Open", "Save", "Exit"]:
    tk.Button(toolbar, text=name).pack(side="left", padx=4, pady=4)

root.mainloop()
