# task22_canvas_draw_circle.py
import tkinter as tk

def draw_circle(event):
    r = 5
    canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="blue")

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()
canvas.bind("<Button-1>", draw_circle)
root.mainloop()
