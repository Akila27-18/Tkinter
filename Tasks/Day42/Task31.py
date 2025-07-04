import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Fruit Combobox")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Select a fruit:")
label.pack(pady=10)

# Create Combobox
fruits = ["Apple", "Banana", "Cherry"]
combo = ttk.Combobox(root, values=fruits, state="readonly")
combo.pack(pady=10)

# Optional: Set default value
combo.current(0)  # Select "Apple" by default

root.mainloop()
