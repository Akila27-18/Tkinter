import tkinter as tk
from tkinter import ttk

# Sample customer data
customers = {
    "C001": {"name": "Alice Smith", "contact": "9876543210", "address": "123 Main Street"},
    "C002": {"name": "Bob Johnson", "contact": "8765432109", "address": "456 Elm Avenue"},
    "C003": {"name": "Charlie Lee", "contact": "7654321098", "address": "789 Oak Road"},
    "C004": {"name": "Diana Rose", "contact": "6543210987", "address": "321 Pine Blvd"}
}

def on_customer_select(event):
    customer_id = combo_customer.get()
    if customer_id in customers:
        data = customers[customer_id]
        label_name.config(text=f"Name: {data['name']}")
        label_contact.config(text=f"Contact: {data['contact']}")
        label_address.config(text=f"Address: {data['address']}")
        if disable_var.get():
            combo_customer.config(state="disabled")

def reset_selection():
    combo_customer.config(state="readonly")
    combo_customer.set('')
    label_name.config(text="Name: ")
    label_contact.config(text="Contact: ")
    label_address.config(text="Address: ")

# Main window
root = tk.Tk()
root.title("Customer Drop-down Selector")
root.geometry("400x300")

# Combobox label
tk.Label(root, text="Select Customer ID:").pack(pady=5)

# Combobox
combo_customer = ttk.Combobox(root, values=list(customers.keys()), state="readonly")
combo_customer.pack()
combo_customer.bind("<<ComboboxSelected>>", on_customer_select)

# Labels for displaying info
label_name = tk.Label(root, text="Name: ", font=("Arial", 12))
label_name.pack(pady=5)

label_contact = tk.Label(root, text="Contact: ", font=("Arial", 12))
label_contact.pack(pady=5)

label_address = tk.Label(root, text="Address: ", font=("Arial", 12))
label_address.pack(pady=5)

# Checkbox to disable after selection
disable_var = tk.BooleanVar()
check_disable = tk.Checkbutton(root, text="Disable dropdown after selection", variable=disable_var)
check_disable.pack(pady=5)

# Reset button
btn_reset = tk.Button(root, text="Reset", command=reset_selection)
btn_reset.pack(pady=10)

root.mainloop()
