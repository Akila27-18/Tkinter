import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Positioned Window")

# Set size and position: width x height + x_offset + y_offset
root.geometry("300x200+200+100")

# Optional: Add a label
label = tk.Label(root, text="Window at (200, 100)", font=("Arial", 12))
label.pack(pady=80)

# Start the event loop
root.mainloop()
