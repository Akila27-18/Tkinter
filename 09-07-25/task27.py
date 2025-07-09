# task27_display_keysym.py
import tkinter as tk

def show_key(event):
    label.config(text=f"Key: {event.keysym}")

root = tk.Tk()
label = tk.Label(root, text="Press any key", font=("Arial", 16))
label.pack(pady=30)
root.bind("<KeyPress>", show_key)
root.mainloop()
