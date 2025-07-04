import tkinter as tk

def draw_shapes(canvas):
    canvas.delete("all")  # Clear canvas

# 1. Custom canvas size
root = tk.Tk()
root.title("Canvas Positioning & Dimensions")
root.geometry("600x500")

# Create Canvas
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=10)

# Initial draw
draw_shapes(canvas)

root.mainloop()
