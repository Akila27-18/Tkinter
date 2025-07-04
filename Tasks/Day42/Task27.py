import tkinter as tk

root = tk.Tk()
root.title("Horizontal Scrollbar Example")

# Frame to hold Listbox and Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a horizontal scrollbar
h_scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Create the Listbox with extended width and xscrollcommand
listbox = tk.Listbox(frame, width=50, xscrollcommand=h_scroll.set)
listbox.pack()

# Configure scrollbar to work with listbox
h_scroll.config(command=listbox.xview)

# Add long text items to the Listbox
long_items = [
    "This is a very long item that will not fit in the listbox width",
    "Another extremely lengthy item that requires scrolling to view completely",
    "Short",
    "Yet another super long listbox entry that tests horizontal scrolling"
]

for item in long_items:
    listbox.insert(tk.END, item)

root.mainloop()
