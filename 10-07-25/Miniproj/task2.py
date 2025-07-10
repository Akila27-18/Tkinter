import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Globals
current_file = None

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        title="Open Text File",
        filetypes=[("Text Files", "*.txt")]
    )
    if not file_path:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
            current_file = file_path
            root.title(f"Text Editor - {os.path.basename(file_path)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file:\n{e}")

def save_file():
    global current_file
    content = text_area.get(1.0, tk.END).strip()

    if not content:
        messagebox.showwarning("Empty Content", "Cannot save empty file.")
        return

    if current_file:
        path = current_file
    else:
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if not path:
            return

    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        current_file = path
        messagebox.showinfo("Success", f"File saved to:\n{path}")
        root.title(f"Text Editor - {os.path.basename(path)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Text Editor")
root.geometry("600x500")

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

text_area = tk.Text(root, wrap='word', font=("Arial", 12))
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
