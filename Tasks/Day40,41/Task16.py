import tkinter as tk
from tkinter import messagebox

# Function to show a message box
def show_message():
    messagebox.showinfo("Greetings", "Hello! This is a message box.")

# Create main window
root = tk.Tk()
root.title("Message Box Example")
root.geometry("300x150")

# Create button
btn = tk.Button(root, text="Show Message", command=show_message)
btn.pack(pady=40)

# Start the event loop
root.mainloop()
