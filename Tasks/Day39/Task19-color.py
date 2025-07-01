import tkinter as tk

# Main window
root = tk.Tk()
root.title("Custom Label")
root.geometry("300x150")

# Customized Label
label = tk.Label(root, 
                 text="Hello, Tkinter!",
                 font=("Arial", 16, "bold"),  # Font family, size, style
                 fg="blue")  # Text color
label.pack(pady=20)

root.mainloop()
