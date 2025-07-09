# task43_color_picker.py
import tkinter as tk

class ColorPicker(tk.Frame):
    def __init__(self, master, colors, on_pick, **kwargs):
        super().__init__(master, **kwargs)
        for color in colors:
            tk.Button(self, bg=color, width=4, command=lambda c=color: on_pick(c)).pack(side="left", padx=2)

def pick_color(c): print(f"Picked color: {c}")

root = tk.Tk()
widget = ColorPicker(root, ["red", "green", "blue", "yellow", "purple"], on_pick=pick_color)
widget.pack(pady=10)
root.mainloop()
