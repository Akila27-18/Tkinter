import tkinter as tk

# Constants
MOVE_STEP = 10
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

def move_object(dx, dy):
    # Get current coordinates
    coords = canvas.coords(shape)
    x1, y1, x2, y2 = coords

    # Check boundaries
    if x1 + dx < 0 or x2 + dx > CANVAS_WIDTH:
        dx = 0
    if y1 + dy < 0 or y2 + dy > CANVAS_HEIGHT:
        dy = 0

    # Move if within boundaries
    canvas.move(shape, dx, dy)

def key_handler(event):
    key = event.keysym
    if key == "Left":
        move_object(-MOVE_STEP, 0)
    elif key == "Right":
        move_object(MOVE_STEP, 0)
    elif key == "Up":
        move_object(0, -MOVE_STEP)
    elif key == "Down":
        move_object(0, MOVE_STEP)

# Main window
root = tk.Tk()
root.title("Canvas Object Mover with Keys")

# Canvas setup
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()

# Draw a circle (oval) at the center
shape = canvas.create_oval(170, 120, 210, 160, fill='skyblue')

# Bind arrow keys
root.bind("<KeyPress>", key_handler)
canvas.focus_set()  # Ensure canvas receives key events

root.mainloop()
