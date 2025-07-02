import tkinter as tk

# Function to handle key press
def handle_arrow(event):
    if event.keysym == "Up":
        direction_label.config(text="You pressed: Up")
    elif event.keysym == "Down":
        direction_label.config(text="You pressed: Down")

# Create main window
root = tk.Tk()
root.title("Arrow Key Event")
root.geometry("300x150")

# Label to show direction
direction_label = tk.Label(root, text="Press Up or Down Arrow", font=("Arial", 12))
direction_label.pack(pady=40)

# Bind arrow keys to the root window
root.bind("<Up>", handle_arrow)
root.bind("<Down>", handle_arrow)

# Start the event loop
root.mainloop()
