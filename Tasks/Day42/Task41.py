import tkinter as tk

root = tk.Tk()
root.title("Spinbox Example")
root.geometry("250x150")

# Label
tk.Label(root, text="Select a number (0–100):").pack(pady=10)

# Spinbox from 0 to 100
spin = tk.Spinbox(root, from_=0, to=100, width=10)
spin.pack(pady=5)

root.mainloop()
