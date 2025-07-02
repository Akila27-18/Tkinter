import tkinter as tk
import re

# Validation function using regex
def validate_numeric_input(new_value):
    return re.fullmatch(r'\d*', new_value) is not None  # Allow only digits

# Create main window
root = tk.Tk()
root.title("Numeric Input Only")
root.geometry("300x150")

# Register the validation function
vcmd = (root.register(validate_numeric_input), '%P')

# Label and Entry
tk.Label(root, text="Enter a number:").pack(pady=5)
entry = tk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(pady=10)

# Start the event loop
root.mainloop()
