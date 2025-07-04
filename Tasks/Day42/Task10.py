import tkinter as tk

def draw_shapes(canvas):
    canvas.delete("all")  # Clear canvas

   

def resize_canvas():
    try:
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        canvas.config(width=new_width, height=new_height)
        draw_shapes(canvas)
    except ValueError:
        print("Enter valid integers for width and height.")

# 1. Custom canvas size
root = tk.Tk()
root.title("Canvas Positioning & Dimensions")
root.geometry("600x500")

# Input fields to resize canvas
controls = tk.Frame(root)
controls.pack(pady=10)

tk.Label(controls, text="Width:").grid(row=0, column=0)
width_entry = tk.Entry(controls, width=5)
width_entry.grid(row=0, column=1)
width_entry.insert(0, "400")

tk.Label(controls, text="Height:").grid(row=0, column=2)
height_entry = tk.Entry(controls, width=5)
height_entry.grid(row=0, column=3)
height_entry.insert(0, "300")

tk.Button(controls, text="Resize Canvas", command=resize_canvas).grid(row=0, column=4, padx=10)

# Create Canvas
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=10)

# Initial draw
draw_shapes(canvas)

root.mainloop()
