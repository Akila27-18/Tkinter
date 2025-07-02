import tkinter as tk

# Function to handle key press
def key_pressed(event):
    print(f"Key pressed: {event.char} (KeyCode: {event.keycode})")

# Create main window
root = tk.Tk()
root.title("Key Press Event")
root.geometry("300x100")

# Instruction label
label = tk.Label(root, text="Press any key...")
label.pack(pady=30)

# Bind key press event to the root window
root.bind("<Key>", key_pressed)

# Start the event loop
root.mainloop()
