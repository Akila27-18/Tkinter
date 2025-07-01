import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Window with Custom Icon")
root.geometry("300x150")

# Load the PNG image
icon = PhotoImage(file=r"C:\Users\sharm\Desktop\Zahirx\Images\Group 24.png")

# Set it as the window icon
root.iconphoto(False, icon)

# Add sample content
tk.Label(root, text="Custom icon set!").pack(pady=20)

root.mainloop()
