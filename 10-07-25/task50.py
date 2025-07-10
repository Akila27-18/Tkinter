import tkinter as tk
from tkinter import filedialog, messagebox

def import_txt():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        try:
            with open(path, "r") as f:
                lines = f.readlines()
                if len(lines) >= 3:
                    entry_name.delete(0, tk.END)
                    entry_name.insert(0, lines[0].strip())

                    entry_age.delete(0, tk.END)
                    entry_age.insert(0, lines[1].strip())

                    entry_email.delete(0, tk.END)
                    entry_email.insert(0, lines[2].strip())
                else:
                    messagebox.showerror("Error", "File must have at least 3 lines (Name, Age, Email)")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")

root = tk.Tk()
root.title("Import Registration Info")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

tk.Button(root, text="Import from .txt", command=import_txt).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
