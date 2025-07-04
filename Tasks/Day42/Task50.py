import tkinter as tk
from tkinter import ttk

def show_selection():
    item = item_var.get()
    qty = qty_var.get()
    result_label.config(text=f"Selected: {item} x {qty}")

root = tk.Tk()
root.title("Item and Quantity Selector")
root.geometry("300x200")

# Combobox for item selection
item_var = tk.StringVar()
items = ["Apples", "Bananas", "Oranges", "Mangoes", "Grapes"]
item_combo = ttk.Combobox(root, textvariable=item_var, values=items, state="readonly")
item_combo.current(0)
item_combo.pack(pady=10)

# Spinbox for quantity selection
qty_var = tk.StringVar(value="1")
qty_spinbox = tk.Spinbox(root, from_=1, to=100, textvariable=qty_var, width=5)
qty_spinbox.pack(pady=10)

# Button to show selection
select_button = tk.Button(root, text="Confirm Selection", command=show_selection)
select_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Selected: None")
result_label.pack(pady=5)

root.mainloop()
