import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Readonly Combobox")
root.geometry("250x150")

# Readonly Combobox
options = ["Option 1", "Option 2", "Option 3"]
combo = ttk.Combobox(root, values=options, state="readonly")
combo.current(0)  # Set default selection
combo.pack(pady=20)

root.mainloop()
