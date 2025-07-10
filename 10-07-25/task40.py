import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv"), ("JSON Files", "*.json")]
    )
    if file_path:
        with open(file_path, "w") as f:
            f.write("Sample data")

root = tk.Tk()
root.title("Save with Filters")

tk.Button(root, text="Save File", command=save_file).pack(padx=20, pady=20)

root.mainloop()
