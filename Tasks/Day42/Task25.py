import tkinter as tk

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Add Item Dynamically")
root.geometry("300x250")

# Entry widget
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Button to add item
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

# Listbox to display items
listbox = tk.Listbox(root, width=30, height=8)
listbox.pack(pady=10)

root.mainloop()
