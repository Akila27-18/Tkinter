import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Vertical Resize Only")
root.geometry("300x200")

# Disable horizontal resizing, allow vertical
root.resizable(False, True)

# Optional label
label = tk.Label(root, text="You can resize vertically only", font=("Arial", 12))
label.pack(pady=60)

# Start the event loop
root.mainloop()
