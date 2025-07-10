import tkinter as tk
from tkinter import filedialog

def choose_dir():
    path = filedialog.askdirectory()
    if path:
        lbl_dir.config(text=path)

root = tk.Tk()
root.title("Choose Directory")

tk.Button(root, text="Choose Folder", command=choose_dir).pack(pady=10)
lbl_dir = tk.Label(root, text="No directory selected")
lbl_dir.pack()

root.mainloop()
