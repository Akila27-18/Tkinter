import tkinter as tk

root = tk.Tk()
root.title("Listbox with Scrollbar")
root.geometry("300x300")

# Create frame to hold Listbox and Scrollbar
frame = tk.Frame(root)
frame.pack(pady=20)

# Create Listbox with height limit
listbox = tk.Listbox(frame, width=30, height=10)
listbox.pack(side=tk.LEFT)

# Create vertical scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Attach scrollbar to Listbox
listbox.config(yscrollcommand=scrollbar.set)

# Insert 20+ items
for i in range(1, 31):
    listbox.insert(tk.END, f"Item {i}")

root.mainloop()
