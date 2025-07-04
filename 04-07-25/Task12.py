import tkinter as tk
from tkinter import simpledialog, messagebox

# Sample 50+ product names
PRODUCTS = [f"Product {i}" for i in range(1, 101)]

def show_details(event):
    selected = listbox.curselection()
    if selected:
        product = listbox.get(selected[0])
        label_detail.config(text=f"Selected: {product}")

def add_product():
    new_product = simpledialog.askstring("Add Product", "Enter product name:")
    if new_product:
        listbox.insert(tk.END, new_product)

def delete_product():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
        label_detail.config(text="Deleted product.")
    else:
        messagebox.showwarning("No Selection", "Please select a product to delete.")

# Main window
root = tk.Tk()
root.title("Scrollable Product List")
root.geometry("400x400")

# Frame for Listbox and Scrollbar
frame_list = tk.Frame(root)
frame_list.pack(pady=10, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
listbox = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, height=15)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Insert products into listbox
for product in PRODUCTS:
    listbox.insert(tk.END, product)

# Bind click event
listbox.bind('<<ListboxSelect>>', show_details)

# Detail label
label_detail = tk.Label(root, text="Select a product to view details", font=("Arial", 12))
label_detail.pack(pady=5)

# Frame for buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# Add Button
btn_add = tk.Button(frame_buttons, text="Add Product", command=add_product)
btn_add.pack(side=tk.LEFT, padx=10)

# Delete Button
btn_delete = tk.Button(frame_buttons, text="Delete Product", command=delete_product)
btn_delete.pack(side=tk.LEFT, padx=10)

root.mainloop()
