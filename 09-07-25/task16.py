# task16_click_coords.py
import tkinter as tk

def on_click(event):
    print(f"Clicked at: ({event.x}, {event.y})")

root = tk.Tk()
btn = tk.Button(root, text="Click Me")
btn.bind("<Button-1>", on_click)
btn.pack(pady=20)
root.mainloop()
