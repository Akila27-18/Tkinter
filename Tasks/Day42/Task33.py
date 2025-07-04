import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox with Default Selection")

# Create Combobox with options
options = ["Red", "Green", "Blue", "Yellow"]
combo = ttk.Combobox(root, values=options)
combo.pack(padx=10, pady=10)

# Set default selection (e.g., "Green" → index 1)
combo.current(1)

root.mainloop()
