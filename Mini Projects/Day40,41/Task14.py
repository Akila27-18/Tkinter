import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry_item.get().strip()
    qty = entry_qty.get().strip()
    price = entry_price.get().strip()

    # Validation
    if not item or not qty or not price:
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    if not qty.isdigit() or not price.replace('.', '', 1).isdigit():
        messagebox.showwarning("Input Error", "Quantity and Price must be numeric.")
        return

    qty = int(qty)
    price = float(price)
    total = qty * price

    # Display in Text widget
    output_text.insert(tk.END, f"{item:<15} Qty: {qty:<5} Price: ₹{price:<7} Total: ₹{total:.2f}\n")

    # Clear entries
    entry_item.delete(0, tk.END)
    entry_qty.delete(0, tk.END)
    entry_price.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Inventory Input Form")
root.geometry("500x350")

# Labels and Entry Fields
tk.Label(root, text="Item Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_item = tk.Entry(root, width=30)
entry_item.grid(row=0, column=1)

tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_qty = tk.Entry(root, width=30)
entry_qty.grid(row=1, column=1)

tk.Label(root, text="Price (₹):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_price = tk.Entry(root, width=30)
entry_price.grid(row=2, column=1)

# Add Item Button
tk.Button(root, text="Add Item", command=add_item).grid(row=3, columnspan=2, pady=10)

# Output Text Widget
output_text = tk.Text(root, width=60, height=10)
output_text.grid(row=4, columnspan=2, padx=10, pady=10)

# Add header
output_text.insert(tk.END, f"{'Item':<15} Qty   Price     Total\n")
output_text.insert(tk.END, "-"*50 + "\n")

root.mainloop()
