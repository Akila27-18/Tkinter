import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Centered Window")

# Desired window size
window_width = 400
window_height = 300

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position x, y to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Start the event loop
root.mainloop()
