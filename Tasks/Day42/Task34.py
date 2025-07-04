import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox with Typing Enabled")

# Create a Combobox with typing allowed
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"], state="normal")
combo.pack(pady=10)

# Optional: Print selected or typed value
def show_selection():
    print("Selected:", combo.get())

btn = tk.Button(root, text="Show Selection", command=show_selection)
btn.pack(pady=5)

root.mainloop()
