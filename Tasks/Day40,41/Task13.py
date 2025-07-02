import tkinter as tk

# Function to change label text on click
def on_label_click(event):
    label.config(text="Label Clicked!")

# Create main window
root = tk.Tk()
root.title("Label Click Event")
root.geometry("250x100")

# Create label
label = tk.Label(root, text="Click Me", font=("Arial", 14), fg="blue", cursor="hand2")
label.pack(pady=30)

# Bind left mouse click event to the label
label.bind("<Button-1>", on_label_click)

# Start the event loop
root.mainloop()
