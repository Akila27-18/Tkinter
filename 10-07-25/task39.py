import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_widget.get("1.0", tk.END))

root = tk.Tk()
root.title("Save Text to File")

text_widget = tk.Text(root, width=60, height=20)
text_widget.pack(padx=10, pady=10)

tk.Button(root, text="Save", command=save_file).pack()

root.mainloop()
