import tkinter as tk

def show_selected():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        print("Selected item:", item)
    else:
        print("No item selected")

root = tk.Tk()
root.title("Select and Print Item")

# Create a Listbox
listbox = tk.Listbox(root)
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)

# Button to print selected item
button = tk.Button(root, text="Show Selected", command=show_selected)
button.pack(pady=5)

root.mainloop()
