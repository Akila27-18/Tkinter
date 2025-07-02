import tkinter as tk
from tkinter import messagebox

# Function to validate name and submit
def submit():
    name = entry.get().strip()
    if not name:
        messagebox.showwarning("Validation Error", "Name field cannot be empty.")
    else:
        print("Name submitted:", name)

# Create main window
root = tk.Tk()
root.title("Name Validation")
root.geometry("300x150")

# Entry for name
tk.Label(root, text="Enter your name:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=10)

# Start the event loop
root.mainloop()
