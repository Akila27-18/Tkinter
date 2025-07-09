# task32_esc_close.py
import tkinter as tk

def close(event):
    root.destroy()

root = tk.Tk()
root.bind("<Escape>", close)
tk.Label(root, text="Press Esc to close").pack(pady=20)
root.mainloop()
