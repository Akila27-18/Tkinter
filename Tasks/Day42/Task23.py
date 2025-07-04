import tkinter as tk

def show_selected():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Selected items:", selected_items)

root = tk.Tk()
root.title("Multiple Selection Listbox")

# Create a Listbox with MULTIPLE selection mode
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=30, height=10)
listbox.pack(padx=10, pady=10)

# Insert sample items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grapes"]
for item in items:
    listbox.insert(tk.END, item)

# Button to show selected items
btn = tk.Button(root, text="Show Selected", command=show_selected)
btn.pack(pady=10)

root.mainloop()
