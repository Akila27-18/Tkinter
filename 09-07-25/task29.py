# task29_canvas_arrow_move.py
import tkinter as tk

def move(event):
    delta = {"Left": (-10, 0), "Right": (10, 0), "Up": (0, -10), "Down": (0, 10)}
    dx, dy = delta.get(event.keysym, (0, 0))
    canvas.move(rect, dx, dy)

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()
rect = canvas.create_rectangle(140, 140, 160, 160, fill="blue")
root.bind("<KeyPress>", move)
root.mainloop()
