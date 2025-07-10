import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        lbl_path.config(text=file_path)

root = tk.Tk()
root.title("Open File Dialog")

tk.Button(root, text="Open File", command=open_file).pack(pady=10)
lbl_path = tk.Label(root, text="No file selected")
lbl_path.pack()

root.mainloop()
