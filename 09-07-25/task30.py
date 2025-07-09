# task30_toggle_bg_color.py
import tkinter as tk

def toggle_bg(event):
    if event.char.lower() == "b":
        root.config(bg="black")
    elif event.char.lower() == "w":
        root.config(bg="white")

root = tk.Tk()
root.geometry("200x100")
root.bind("<KeyPress>", toggle_bg)
root.mainloop()
