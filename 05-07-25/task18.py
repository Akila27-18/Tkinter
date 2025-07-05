import tkinter as tk
from tkinter import ttk, messagebox

# --- Submit Function with Validation ---
def submit_order():
    name = name_entry.get().strip()
    product = product_box.get().strip()
    quantity = quantity_spin.get()

    # Validate inputs
    if not name:
        messagebox.showwarning("Input Error", "Please enter customer name.")
        return
    if not product:
        messagebox.showwarning("Input Error", "Please select a product.")
        return

    order = f"{name} ordered {quantity} x {product}"
    order_listbox.insert(tk.END, order)
    name_entry.delete(0, tk.END)
    product_box.set("")
    quantity_spin.delete(0, tk.END)
    quantity_spin.insert(0, "1")

# --- Main Window ---
root = tk.Tk()
root.title("Customer Order Form")
root.geometry("450x300")

# --- Form Frame ---
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

# Name
tk.Label(form_frame, text="Customer Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Product
tk.Label(form_frame, text="Product:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
product_box = ttk.Combobox(form_frame, values=["Apples", "Bananas", "Cherries", "Dates"], state="readonly")
product_box.grid(row=1, column=1, padx=5, pady=5)

# Quantity
tk.Label(form_frame, text="Quantity:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
quantity_spin = tk.Spinbox(form_frame, from_=1, to=100, width=5)
quantity_spin.grid(row=2, column=1, padx=5, pady=5)
quantity_spin.delete(0, tk.END)
quantity_spin.insert(0, "1")

# Submit Button
submit_btn = tk.Button(form_frame, text="Submit Order", command=submit_order)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# --- Order List Display ---
list_frame = tk.Frame(root)
list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

order_listbox = tk.Listbox(list_frame, height=8)
order_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=order_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
order_listbox.config(yscrollcommand=scrollbar.set)

# --- Run App ---
root.mainloop()
