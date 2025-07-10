import tkinter as tk
from tkinter import filedialog, messagebox

current_file = None

def open_file():
    global current_file
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "r") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())
        current_file = path
        root.title(f"Notepad - {path}")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as f:
            f.write(text.get("1.0", tk.END))
    else:
        save_as_file()

def save_as_file():
    global current_file
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "w") as f:
            f.write(text.get("1.0", tk.END))
        current_file = path
        root.title(f"Notepad - {path}")

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root, width=60, height=20)
text.pack(padx=10, pady=10)

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)

root.mainloop()
