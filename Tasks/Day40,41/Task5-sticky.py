import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Right-Aligned Label")

# Create a label and an entry field
label = tk.Label(root, text="Username:")
entry = tk.Entry(root)

# Place them using grid, aligning the label to the right
label.grid(row=0, column=0, padx=10, pady=10, sticky='E')  # Align to East (right)
entry.grid(row=0, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
