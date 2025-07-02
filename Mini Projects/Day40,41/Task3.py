import tkinter as tk
from tkinter import messagebox

# Product data (name, price)
products = [
    ("Apple", 20),
    ("Banana", 10),
    ("Orange", 15)
]

def calculate_total():
    total = 0
    for i, (_, price) in enumerate(products):
        qty = qty_vars[i].get()
        if qty.isdigit():
            total += int(qty) * price
        elif qty.strip() != "":
            messagebox.showwarning("Invalid Input", f"Enter a valid number for {products[i][0]}")
            return
    total_label.config(text=f"Total: ₹{total}")

def place_order():
    order_details = []
    for i, (name, price) in enumerate(products):
        qty = qty_vars[i].get()
        if qty.isdigit() and int(qty) > 0:
            order_details.append(f"{name} x {qty} = ₹{int(qty)*price}")
    if order_details:
        messagebox.showinfo("Order Placed", "\n".join(order_details) + f"\n\n{total_label.cget('text')}")
    else:
        messagebox.showwarning("No Order", "Please enter quantity for at least one product.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Product Order Form")
root.geometry("350x250")

# Quantity input variables
qty_vars = [tk.StringVar(value="0") for _ in products]

# Create header
tk.Label(root, text="Product").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Price (₹)").grid(row=0, column=1, padx=10)
tk.Label(root, text="Quantity").grid(row=0, column=2, padx=10)

# Product rows
for i, (name, price) in enumerate(products):
    tk.Label(root, text=name).grid(row=i+1, column=0)
    tk.Label(root, text=f"₹{price}").grid(row=i+1, column=1)
    tk.Entry(root, textvariable=qty_vars[i], width=8).grid(row=i+1, column=2)

# Total label
total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 12, "bold"))
total_label.grid(row=len(products)+1, columnspan=3, pady=10)

# Buttons
tk.Button(root, text="Calculate Total", command=calculate_total).grid(row=len(products)+2, column=0, pady=10)
tk.Button(root, text="Place Order", command=place_order).grid(row=len(products)+2, column=2)

root.mainloop()
