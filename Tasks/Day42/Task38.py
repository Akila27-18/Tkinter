import tkinter as tk
from tkinter import ttk

def reset_combobox():
    # Reset to default (e.g., index 0)
    combo.current(0)

root = tk.Tk()
root.title("Reset Combobox")

# Combobox options
options = ["Select a color", "Red", "Green", "Blue"]
combo = ttk.Combobox(root, values=options, state="readonly")
combo.pack(padx=10, pady=10)

# Set default selection (first item: "Select a color")
combo.current(0)

# Button to reset Combobox
btn_reset = tk.Button(root, text="Reset", command=reset_combobox)
btn_reset.pack(pady=10)

root.mainloop()
