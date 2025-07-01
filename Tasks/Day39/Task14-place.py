import tkinter as tk

# Create main window
root = tk.Tk()
root.title("place() Layout Example")
root.geometry("300x150")  # Set window size

# Button placed at x=100, y=50
button = tk.Button(root, text="Click Me")
button.place(x=100, y=50)

root.mainloop()
