import tkinter as tk

# Function to update label with mouse coordinates
def show_mouse_position(event):
    coords = f"Mouse at: x={event.x}, y={event.y}"
    position_label.config(text=coords)

# Create main window
root = tk.Tk()
root.title("Mouse Tracker")
root.geometry("400x200")

# Label to display coordinates
position_label = tk.Label(root, text="Move your mouse inside the window", font=("Arial", 12))
position_label.pack(pady=60)

# Bind mouse motion event to the window
root.bind("<Motion>", show_mouse_position)

# Start the event loop
root.mainloop()
