import tkinter as tk
import platform

# Create main window
root = tk.Tk()
root.title("Maximized Window Example")

# Maximize window if on Windows
if platform.system() == "Windows":
    root.state('zoomed')  # Maximized mode
else:
    root.attributes('-zoomed', True)  # Some Linux systems

# Optional content
label = tk.Label(root, text="This window opens maximized", font=("Arial", 16))
label.pack(pady=100)

# Start event loop
root.mainloop()
