import tkinter as tk

def scroll_to_item():
    listbox.see(9)  # Index starts at 0, so Item 10 is at index 9
    listbox.selection_clear(0, tk.END)
    listbox.selection_set(9)
    listbox.activate(9)

root = tk.Tk()
root.title("Scroll to Specific Item")

# Create a Listbox and populate with many items
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

for i in range(1, 31):
    listbox.insert(tk.END, f"Item {i}")

# Button to scroll to Item 10
scroll_button = tk.Button(root, text="Go to Item 10", command=scroll_to_item)
scroll_button.pack(pady=5)

root.mainloop()
