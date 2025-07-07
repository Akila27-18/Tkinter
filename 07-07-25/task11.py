import tkinter as tk
from tkinter import ttk

# Sample product list
products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]

# Function to add order
def add_order():
    product = product_combo.get()
    quantity = quantity_spinbox.get()

    if not product or not quantity.isdigit() or int(quantity) <= 0:
        status_label.config(text="Select a product and enter a valid quantity", fg="red")
    else:
        order = f"{product} - Quantity: {quantity}"
        order_listbox.insert(tk.END, order)
        status_label.config(text="Order added!", fg="green")
        product_combo.set("")
        quantity_spinbox.delete(0, tk.END)
        quantity_spinbox.insert(0, "1")

# Main window
root = tk.Tk()
root.title("Product Order Form")
root.geometry("500x350")

# ========== Input Frame ==========
input_frame = tk.LabelFrame(root, text="Place Your Order", padx=10, pady=10)
input_frame.pack(padx=20, pady=10, fill="x")

# Product Combobox
tk.Label(input_frame, text="Select Product:").grid(row=0, column=0, sticky="e")
product_combo = ttk.Combobox(input_frame, values=products, state="readonly", width=30)
product_combo.grid(row=0, column=1, pady=5)

# Quantity Spinbox
tk.Label(input_frame, text="Quantity:").grid(row=1, column=0, sticky="e")
quantity_spinbox = tk.Spinbox(input_frame, from_=1, to=100, width=5)
quantity_spinbox.grid(row=1, column=1, sticky="w")
quantity_spinbox.delete(0, tk.END)
quantity_spinbox.insert(0, "1")

# Submit Button
submit_button = tk.Button(input_frame, text="Add to Order", command=add_order)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Status Label
status_label = tk.Label(input_frame, text="", fg="green")
status_label.grid(row=3, column=0, columnspan=2)

# ========== Order List Frame ==========
list_frame = tk.LabelFrame(root, text="Order Summary", padx=10, pady=10)
list_frame.pack(padx=20, pady=10, fill="both", expand=True)

order_listbox = tk.Listbox(list_frame)
order_listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

order_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=order_listbox.yview)

root.mainloop()
