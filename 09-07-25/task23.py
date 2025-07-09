# task23_canvas_draw_rectangle.py
import tkinter as tk

points = []

def draw_rectangle(event):
    points.append((event.x, event.y))
    if len(points) == 2:
        canvas.create_rectangle(*points[0], *points[1], outline="red")
        points.clear()

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()
canvas.bind("<Button-1>", draw_rectangle)
root.mainloop()
