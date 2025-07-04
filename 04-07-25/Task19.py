import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def apply_settings():
    title = entry_title.get()
    width = entry_width.get()
    height = entry_height.get()

    if not width.isdigit() or not height.isdigit():
        messagebox.showerror("Invalid Input", "Width and Height must be numbers.")
        return

    root.title(title)
    root.geometry(f"{width}x{height}")

    if icon_path.get():
        try:
            root.iconbitmap(icon_path.get())
        except Exception as e:
            messagebox.showerror("Icon Error", f"Failed to set icon:\n{e}")

def browse_icon():
    path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    if path:
        icon_path.set(path)

# Main window
root = tk.Tk()
root.title("Window Configurator")
root.geometry("400x300")

# Variables
icon_path = tk.StringVar()

# Title
ttk.Label(root, text="Window Title:").place(x=30, y=30)
entry_title = ttk.Entry(root, width=25)
entry_title.place(x=150, y=30)

# Width
ttk.Label(root, text="Width:").place(x=30, y=70)
entry_width = ttk.Entry(root, width=10)
entry_width.place(x=150, y=70)

# Height
ttk.Label(root, text="Height:").place(x=220, y=70)
entry_height = ttk.Entry(root, width=10)
entry_height.place(x=280, y=70)

# Icon
ttk.Label(root, text="Icon (.ico):").place(x=30, y=110)
entry_icon = ttk.Entry(root, textvariable=icon_path, width=25)
entry_icon.place(x=150, y=110)
ttk.Button(root, text="Browse", command=browse_icon).place(x=310, y=108)

# Apply Button
ttk.Button(root, text="Apply Settings", command=apply_settings).place(x=150, y=160)

root.mainloop()
