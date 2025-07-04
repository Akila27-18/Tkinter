import tkinter as tk
from tkinter import ttk

class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Order Interface")

        # Product data
        self.products = {
            "Fruits": ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Strawberry", "Papaya"],
            "Vegetables": ["Tomato", "Potato", "Carrot", "Cabbage", "Broccoli", "Spinach", "Onion", "Beans"],
            "Drinks": ["Water", "Juice", "Soda", "Milk", "Tea", "Coffee", "Smoothie", "Lassi"]
        }

        # Top Frame (Category + Product List)
        top_frame = tk.Frame(root)
        top_frame.pack(pady=5)

        # Category Combobox
        tk.Label(top_frame, text="Select Category:").grid(row=0, column=0, padx=5)
        self.category_var = tk.StringVar()
        self.category_cb = ttk.Combobox(top_frame, textvariable=self.category_var,
                                        values=list(self.products.keys()), state="readonly", width=15)
        self.category_cb.grid(row=0, column=1, padx=5)
        self.category_cb.bind("<<ComboboxSelected>>", self.load_products)
        self.category_cb.set("Fruits")

        # Product Listbox + Scrollbar
        product_frame = tk.Frame(top_frame)
        product_frame.grid(row=0, column=2, padx=10)

        self.product_listbox = tk.Listbox(product_frame, height=8, width=20, exportselection=False)
        self.product_listbox.pack(side=tk.LEFT)

        prod_scroll = tk.Scrollbar(product_frame, orient=tk.VERTICAL, command=self.product_listbox.yview)
        self.product_listbox.config(yscrollcommand=prod_scroll.set)
        prod_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Quantity Spinbox
        tk.Label(top_frame, text="Quantity:").grid(row=0, column=3, padx=5)
        self.qty_spin = tk.Spinbox(top_frame, from_=1, to=100, width=5)
        self.qty_spin.grid(row=0, column=4, padx=5)

        # Add to Cart Button
        add_btn = tk.Button(top_frame, text="Add to Cart", command=self.add_to_cart)
        add_btn.grid(row=0, column=5, padx=10)

        # Cart Label
        tk.Label(root, text="Cart Items:").pack()

        # Cart Listbox + Scrollbar
        cart_frame = tk.Frame(root)
        cart_frame.pack()

        self.cart_listbox = tk.Listbox(cart_frame, height=8, width=50)
        self.cart_listbox.pack(side=tk.LEFT)

        cart_scroll = tk.Scrollbar(cart_frame, orient=tk.VERTICAL, command=self.cart_listbox.yview)
        self.cart_listbox.config(yscrollcommand=cart_scroll.set)
        cart_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Load initial products
        self.load_products()

    def load_products(self, event=None):
        category = self.category_var.get()
        self.product_listbox.delete(0, tk.END)
        for item in self.products.get(category, []):
            self.product_listbox.insert(tk.END, item)

    def add_to_cart(self):
        selection = self.product_listbox.curselection()
        if not selection:
            return
        product = self.product_listbox.get(selection[0])
        qty = self.qty_spin.get()
        self.cart_listbox.insert(tk.END, f"{product} x {qty}")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()
