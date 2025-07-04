import tkinter as tk

root = tk.Tk()
root.title("Spinbox Step by 5")

# Create Spinbox with step size of 5
spin = tk.Spinbox(root, from_=0, to=100, increment=5, width=10)
spin.pack(pady=20)

root.mainloop()
