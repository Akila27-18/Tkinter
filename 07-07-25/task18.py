import tkinter as tk
from tkinter import messagebox

# Dictionary to track stock
stock_data = {}

def add_item():
    item = item_entry.get().strip()
    try:
        qty = int(quantity_spinbox.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Quantity must be a number.")
        return

    if not item:
        messagebox.showwarning("Missing Info", "Item name cannot be empty.")
        return
    if qty <= 0:
        messagebox.showwarning("Invalid Quantity", "Quantity must be greater than 0.")
        return

    # Add or update stock
    stock_data[item] = stock_data.get(item, 0) + qty
    update_listbox()

    item_entry.delete(0, tk.END)
    quantity_spinbox.delete(0, tk.END)
    quantity_spinbox.insert(0, "1")

def update_listbox():
    stock_listbox.delete(0, tk.END)
    for item, qty in stock_data.items():
        stock_listbox.insert(tk.END, f"{item}: {qty}")

# Create window
root = tk.Tk()
root.title("Inventory Stock Tracker")
root.geometry("400x400")

# Item Entry
tk.Label(root, text="Item Name:").place(x=20, y=20)
item_entry = tk.Entry(root, width=30)
item_entry.place(x=120, y=20)

# Quantity Spinbox
tk.Label(root, text="Quantity:").place(x=20, y=60)
quantity_spinbox = tk.Spinbox(root, from_=1, to=1000, width=5)
quantity_spinbox.place(x=120, y=60)

# Add Button
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.place(x=200, y=58)

# Listbox with Scrollbar
tk.Label(root, text="Current Stock:").place(x=20, y=110)
frame = tk.Frame(root)
frame.place(x=20, y=140, width=360, height=220)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

stock_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=50, height=12)
stock_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=stock_listbox.yview)

# Start the GUI
root.mainloop()
