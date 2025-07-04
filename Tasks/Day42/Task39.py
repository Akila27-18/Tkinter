import tkinter as tk
from tkinter import ttk

def update_label(event=None):
    selected = combo.get()
    label.config(text=f"Selected: {selected}")

root = tk.Tk()
root.title("Combobox Selection Display")

# Combobox with options and typing allowed
combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"], state="normal")
combo.pack(pady=10)
combo.bind("<<ComboboxSelected>>", update_label)

# Label to display selected item
label = tk.Label(root, text="Selected: None")
label.pack(pady=5)

# Also update when user types and clicks a button (optional)
btn = tk.Button(root, text="Confirm Selection", command=update_label)
btn.pack(pady=5)

root.mainloop()
