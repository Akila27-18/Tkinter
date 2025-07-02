import tkinter as tk

# Function to run when button is clicked
def say_hello():
    print("Hello! Button was clicked.")

# Create main window
root = tk.Tk()
root.title("Button Click Example")
root.geometry("200x100")

# Create button
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=20)

# Start the event loop
root.mainloop()
