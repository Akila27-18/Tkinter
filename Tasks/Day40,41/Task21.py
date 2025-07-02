import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Fixed Size Window")

# Set fixed window size
root.geometry("400x300")

# Disable window resizing
root.resizable(False, False)

# Optional: Add a label
label = tk.Label(root, text="This window is fixed size.", font=("Arial", 12))
label.pack(pady=120)

# Start the event loop
root.mainloop()
