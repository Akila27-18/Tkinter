import tkinter as tk

def draw_shapes(canvas):
    canvas.delete("all")  # Clear canvas

    # Dynamic coordinates
    x1, y1 = 50, 50
    x2, y2 = 150, 120
    center_x, center_y = 200, 100

    # 2. Text on canvas
    canvas.create_text(center_x, 20, text="Canvas Drawing", font=("Arial", 16), fill="black")

    # 3. Multiple shapes
    canvas.create_rectangle(x1, y1, x2, y2, fill="skyblue", outline="black")
    canvas.create_oval(x1+170, y1, x2+170, y2, fill="lightgreen", outline="green")
    canvas.create_line(x1, y1+150, x2+170, y2+150, fill="red", width=2)

 


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
