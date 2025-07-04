import tkinter as tk

root = tk.Tk()
root.title("Quantity Selector")

# Label
tk.Label(root, text="Select Quantity (1–10):").pack(pady=(10, 0))

# Spinbox for quantity selection
quantity_spin = tk.Spinbox(root, from_=1, to=10, width=5)
quantity_spin.pack(pady=5)

# Show selected quantity
def show_quantity():
    print("Selected Quantity:", quantity_spin.get())

# Button to print the selected value
tk.Button(root, text="Submit", command=show_quantity).pack(pady=10)

root.mainloop()
