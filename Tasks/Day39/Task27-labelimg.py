import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Label with Image")
root.geometry("300x300")

# Load the image (use .png, .gif, etc.)
img = PhotoImage(file=r"C:\Users\sharm\Desktop\Zahirx\Images\Group 24.png")  # Update this path

# Create a label with the image
image_label = tk.Label(root, image=img)
image_label.pack(pady=10)

# Keep a reference to the image (important!)
image_label.image = img

root.mainloop()
