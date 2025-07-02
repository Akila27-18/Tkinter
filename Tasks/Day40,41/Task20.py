import tkinter as tk

# Functions to handle hover events
def on_hover(event):
    button.config(text="You're hovering!")

def on_leave(event):
    button.config(text="Hover Over Me")

# Create main window
root = tk.Tk()
root.title("Hover Button Text")
root.geometry("300x150")

# Create a button
button = tk.Button(root, text="Hover Over Me", font=("Arial", 12))
button.pack(pady=50)

# Bind hover events to the button
button.bind("<Enter>", on_hover)
button.bind("<Leave>", on_leave)

# Start the event loop
root.mainloop()
