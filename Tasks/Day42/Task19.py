import tkinter as tk

def move_shape(event):
    # Get mouse click coordinates
    x, y = event.x, event.y
    # Calculate top-left and bottom-right coordinates of the circle
    r = 20  # radius
    canvas.coords(circle, x - r, y - r, x + r, y + r)

# Create window and canvas
root = tk.Tk()
root.title("Move Shape on Click")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create a circle in the center initially
circle = canvas.create_oval(180, 180, 220, 220, fill="skyblue")

# Bind mouse click to move the shape
canvas.bind("<Button-1>", move_shape)

root.mainloop()
