import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Update Combobox Options")
root.geometry("300x250")

# Initial Combobox values
initial_fruits = ["Apple", "Banana", "Cherry"]

# Create Combobox
combo = ttk.Combobox(root, values=initial_fruits, state="readonly")
combo.pack(pady=20)
combo.set("Select a fruit")

# Function to update Combobox values
def update_fruits():
    new_fruits = ["Mango", "Orange", "Pineapple", "Grapes"]
    combo['values'] = new_fruits
    combo.set("Select a new fruit")

# Button to update options
update_btn = tk.Button(root, text="Update Fruits", command=update_fruits)
update_btn.pack(pady=10)

root.mainloop()
