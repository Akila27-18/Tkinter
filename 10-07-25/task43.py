import tkinter as tk
from tkinter import filedialog

def save_with_default_name():
    file_path = filedialog.asksaveasfilename(
        initialfile="Untitled.txt",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as f:
            f.write("This is a new file with default name.")

root = tk.Tk()
root.title("Save with Default File Name")

tk.Button(root, text="Save As", command=save_with_default_name).pack(pady=20)

root.mainloop()
