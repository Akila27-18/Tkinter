import tkinter as tk

# Function to update label with current window size
def update_size(event):
    width = root.winfo_width()
    height = root.winfo_height()
    size_label.config(text=f"Width: {width}, Height: {height}")

# Create main window
root = tk.Tk()
root.title("Dynamic Size Display")
root.geometry("400x300")

# Label to display size
size_label = tk.Label(root, text="", font=("Arial", 12))
size_label.pack(pady=20)

# Bind resize event to the root window
root.bind("<Configure>", update_size)

# Initial update
update_size(None)

# Start the event loop
root.mainloop()
