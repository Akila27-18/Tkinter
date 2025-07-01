import tkinter as tk

# Create main window
root = tk.Tk()
root.title("grid() Layout Example")
root.geometry("300x100")

# Label in row 0, column 0
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)

# Entry in row 0, column 1
tk.Entry(root, width=25).grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
