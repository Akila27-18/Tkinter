import tkinter as tk

root = tk.Tk()
root.title("Listbox with Static Items")
root.geometry("300x250")

# Create Listbox
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=20)

# Insert static items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for item in items:
    listbox.insert(tk.END, item)

root.mainloop()
