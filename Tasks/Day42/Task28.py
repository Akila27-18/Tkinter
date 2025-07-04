import tkinter as tk

root = tk.Tk()
root.title("Listbox with Scrollbar")

# Frame to hold Listbox and Scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create Listbox
listbox = tk.Listbox(frame, width=30, height=10, selectmode=tk.MULTIPLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create Scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Connect Listbox and Scrollbar
listbox.config(yscrollcommand=scrollbar.set)

# Insert many items for scrolling
for i in range(50):
    listbox.insert(tk.END, f"Item {i+1}")

root.mainloop()
