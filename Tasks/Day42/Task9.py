import tkinter as tk

def draw_shapes(canvas):
    canvas.delete("all")  # Clear canvas

    # Dynamic coordinates
    x1, y1 = 50, 50
    x2, y2 = 150, 120
    center_x, center_y = 200, 100


    # 4. Shape using dynamic coordinates
    triangle_coords = [x1+100, y1+180, x1+130, y1+220, x1+70, y1+220]
    canvas.create_polygon(triangle_coords, fill="orange", outline="black")


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
