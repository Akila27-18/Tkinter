import tkinter as tk
from tkinter import messagebox

def generate_filename():
    project = entry_project.get().strip()
    date = entry_date.get().strip()
    file_type = entry_type.get().strip()

    if not project or not date or not file_type:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    filename = f"{project}_{date}_{file_type}.txt"
    result_label.config(text=f"📄 {filename}")
    
    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(filename)
    messagebox.showinfo("Copied", "File name copied to clipboard!")

# --- GUI Setup ---
root = tk.Tk()
root.title("File Name Generator")
root.geometry("400x250")

# Labels and Entries
tk.Label(root, text="Project Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_project = tk.Entry(root, width=30)
entry_project.grid(row=0, column=1)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_date = tk.Entry(root, width=30)
entry_date.grid(row=1, column=1)

tk.Label(root, text="Type (e.g. report):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_type = tk.Entry(root, width=30)
entry_type.grid(row=2, column=1)

# Generate Button
tk.Button(root, text="Generate File Name", command=generate_filename).grid(row=3, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Courier", 12), fg="blue")
result_label.grid(row=4, columnspan=2, pady=10)

root.mainloop()
