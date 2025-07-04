import tkinter as tk

def clear_listbox():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Clear Listbox Example")

# Create a Listbox and insert some items
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)
listbox.insert(tk.END, "Item 1", "Item 2", "Item 3")

# Create a Button to clear the Listbox
clear_button = tk.Button(root, text="Clear All", command=clear_listbox)
clear_button.pack(pady=5)

root.mainloop()
