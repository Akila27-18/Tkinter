import tkinter as tk
from tkinter import filedialog, messagebox
import os

def apply_changes():
    title = title_entry.get().strip()
    width = width_spin.get().strip()
    height = height_spin.get().strip()
    icon_path = icon_entry.get().strip()

    # Validate title
    if not title:
        messagebox.showerror("Validation Error", "Window title cannot be empty.")
        return

    # Validate width and height
    if not width.isdigit() or not height.isdigit():
        messagebox.showerror("Validation Error", "Width and height must be positive integers.")
        return

    width = int(width)
    height = int(height)

    if width < 100 or height < 100:
        messagebox.showerror("Validation Error", "Width and height must be at least 100.")
        return

    # Apply title and geometry
    root.title(title)
    root.geometry(f"{width}x{height}")

    # Optional: Apply icon
    if icon_path:
        if not os.path.exists(icon_path):
            messagebox.showerror("Icon Error", "Icon file not found.")
            return
        if not icon_path.lower().endswith(".ico"):
            messagebox.showerror("Icon Error", "Icon file must be a .ico file.")
            return
        try:
            root.iconbitmap(icon_path)
        except Exception as e:
            messagebox.showerror("Icon Error", f"Failed to load icon: {e}")

def browse_icon():
    file_path = filedialog.askopenfilename(title="Select Icon", filetypes=[("ICO files", "*.ico")])
    if file_path:
        icon_entry.delete(0, tk.END)
        icon_entry.insert(0, file_path)

# Main window
root = tk.Tk()
root.title("Window Configurator")
root.geometry("400x250")

# Layout
tk.Label(root, text="Window Title:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
title_entry = tk.Entry(root, width=25)
title_entry.grid(row=0, column=1, padx=10)

tk.Label(root, text="Width:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
width_spin = tk.Spinbox(root, from_=100, to=1920, width=10)
width_spin.grid(row=1, column=1, padx=10, sticky='w')

tk.Label(root, text="Height:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
height_spin = tk.Spinbox(root, from_=100, to=1080, width=10)
height_spin.grid(row=2, column=1, padx=10, sticky='w')

tk.Label(root, text="Icon (.ico):").grid(row=3, column=0, padx=10, pady=10, sticky='e')
icon_entry = tk.Entry(root, width=25)
icon_entry.grid(row=3, column=1, padx=10, sticky='w')
tk.Button(root, text="Browse", command=browse_icon).grid(row=3, column=2, padx=5)

tk.Button(root, text="Apply Changes", command=apply_changes, bg="#4CAF50", fg="white").grid(row=4, column=1, pady=20)

root.mainloop()
