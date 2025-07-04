import tkinter as tk

root = tk.Tk()
root.title("Click to Draw Circles")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

def draw_circle(event):
    radius = 20
    x, y = event.x, event.y
    canvas.create_oval(
        x - radius, y - radius,
        x + radius, y + radius,
        fill="skyblue", outline="blue"
    )

# Bind left mouse click to draw_circle
canvas.bind("<Button-1>", draw_circle)

root.mainloop()
