import tkinter as tk
from tkinter import ttk

def draw_shape(event):
    shape = shape_combo.get()
    color = color_combo.get()
    x, y = event.x, event.y

    # Show coordinates
    coord_label.config(text=f"Clicked at: ({x}, {y})")

    size = 40  # fixed shape size

    if shape == "Circle":
        canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline="")
    elif shape == "Rectangle":
        canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=color, outline="")

# Main window
root = tk.Tk()
root.title("Drawing Canvas App")
root.geometry("500x500")

# Top controls frame
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# Shape selector
tk.Label(control_frame, text="Shape:").grid(row=0, column=0, padx=5)
shape_combo = ttk.Combobox(control_frame, values=["Circle", "Rectangle"], state="readonly")
shape_combo.set("Circle")
shape_combo.grid(row=0, column=1, padx=5)

# Color selector
tk.Label(control_frame, text="Color:").grid(row=0, column=2, padx=5)
color_combo = ttk.Combobox(control_frame, values=["red", "blue", "green", "yellow", "black"], state="readonly")
color_combo.set("red")
color_combo.grid(row=0, column=3, padx=5)

# Canvas for drawing
canvas = tk.Canvas(root, bg="white", width=480, height=380)
canvas.pack(pady=10)
canvas.bind("<Button-1>", draw_shape)

# Coordinate label
coord_label = tk.Label(root, text="Clicked at: ")
coord_label.pack()

root.mainloop()
