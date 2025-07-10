import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    try:
        path = filedialog.askopenfilename()
        if not path:
            raise FileNotFoundError("No file selected.")
        with open(path, "r") as f:
            content = f.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "File not selected or invalid path.")

root = tk.Tk()
root.title("Handle File Error")

tk.Button(root, text="Open File", command=open_file).pack(pady=10)

text = tk.Text(root, width=60, height=20)
text.pack(padx=10, pady=10)

root.mainloop()
