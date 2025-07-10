import tkinter as tk
from tkinter import filedialog

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, content)

root = tk.Tk()
root.title("Load Text File")

tk.Button(root, text="Open File", command=load_file).pack()

text_widget = tk.Text(root, width=60, height=20)
text_widget.pack(padx=10, pady=10)

root.mainloop()
