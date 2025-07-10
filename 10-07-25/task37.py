import tkinter as tk
from tkinter import filedialog

def open_txt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        lbl_path.config(text=file_path)

root = tk.Tk()
root.title("Open .txt File")

tk.Button(root, text="Open .txt File", command=open_txt_file).pack(pady=10)
lbl_path = tk.Label(root, text="No file selected")
lbl_path.pack()

root.mainloop()
