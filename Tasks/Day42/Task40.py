import tkinter as tk
from tkinter import ttk

def update_options(event):
    typed = combo_var.get().lower()
    filtered = [item for item in all_options if typed in item.lower()]
    
    combo['values'] = filtered

root = tk.Tk()
root.title("Searchable Combobox")
root.geometry("300x200")

# Full list of options
all_options = ['Apple', 'Banana', 'Orange', 'Grapes', 'Pineapple', 'Watermelon', 'Mango']

# StringVar for tracking input
combo_var = tk.StringVar()

# Editable Combobox
combo = ttk.Combobox(root, textvariable=combo_var)
combo['values'] = all_options
combo.pack(pady=20)

# Bind key release to update options
combo.bind('<KeyRelease>', update_options)

root.mainloop()
