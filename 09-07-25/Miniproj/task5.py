import tkinter as tk

def draw_circle(event):
    x, y = event.x, event.y
    if is_within_bounds(x, y):
        radius = 15
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='skyblue')
        update_label(x, y)
    else:
        coord_label.config(text="Click inside the canvas!")

def draw_rectangle(event):
    x, y = event.x, event.y
    if is_within_bounds(x, y):
        size = 30
        canvas.create_rectangle(x, y, x + size, y + size, fill='lightgreen')
        update_label(x, y)
    else:
        coord_label.config(text="Click inside the canvas!")

def update_label(x, y):
    coord_label.config(text=f"Shape drawn at ({x}, {y})")

def is_within_bounds(x, y):
    return 0 <= x <= canvas.winfo_width() and 0 <= y <= canvas.winfo_height()

# Setup
root = tk.Tk()
root.title("Shape Drawer Canvas")
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white", width=380, height=330, relief='sunken', bd=2)
canvas.pack(pady=10)

coord_label = tk.Label(root, text="Click to draw a shape", font=("Arial", 12))
coord_label.pack()

# Bind events
canvas.bind("<Button-1>", draw_circle)    # Left click
canvas.bind("<Button-3>", draw_rectangle) # Right click

root.mainloop()
