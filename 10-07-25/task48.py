import tkinter as tk
from tkinter import filedialog
import os
import time

def show_file_info():
    path = filedialog.askopenfilename()
    if path:
        size = os.path.getsize(path)
        modified = os.path.getmtime(path)
        lbl_info.config(text=f"Size: {size} bytes\nLast Modified: {time.ctime(modified)}")

root = tk.Tk()
root.title("File Info")

tk.Button(root, text="Select File", command=show_file_info).pack(pady=10)

lbl_info = tk.Label(root, text="")
lbl_info.pack()

root.mainloop()
