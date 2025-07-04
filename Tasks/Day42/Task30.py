import tkinter as tk

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

def show_scroll_position(*args):
    position = listbox.yview()
    scroll_label.config(text=f"Scroll Position: {position[0]:.2f} - {position[1]:.2f}")

root = tk.Tk()
root.title("Listbox Scroll Position")
root.geometry("300x300")

# Entry and Button
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
listbox = tk.Listbox(root, width=30, height=10, yscrollcommand=scrollbar.set)
listbox.pack(pady=5)
scrollbar.config(command=lambda *args: (listbox.yview(*args), show_scroll_position()))

# Scroll position display
scroll_label = tk.Label(root, text="Scroll Position: 0.00 - 1.00")
scroll_label.pack(pady=5)

# Initial data
for i in range(30):
    listbox.insert(tk.END, f"Item {i+1}")

root.mainloop()
