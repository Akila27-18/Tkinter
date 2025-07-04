import tkinter as tk

root = tk.Tk()
root.title("Double Click to Draw Rectangles")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

def draw_rectangle(event):
    width = 40
    height = 30
    x, y = event.x, event.y
    canvas.create_rectangle(
        x - width // 2, y - height // 2,
        x + width // 2, y + height // 2,
        fill="lightgreen", outline="green"
    )

# Bind double left-click to draw_rectangle
canvas.bind("<Double-Button-1>", draw_rectangle)

root.mainloop()
