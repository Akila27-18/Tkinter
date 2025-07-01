import tkinter as tk

root = tk.Tk()
root.title("Fixed Size Window")
root.geometry("300x150")

# Disable resizing (width=False, height=False)
root.resizable(False, False)

tk.Label(root, text="Window cannot be resized.").pack(pady=40)

root.mainloop()
