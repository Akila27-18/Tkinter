import tkinter as tk
from tkinter import ttk

# Draw shape on canvas at mouse click
def draw_shape(event):
    shape = shape_var.get()
    color = color_var.get()
    
    x, y = event.x, event.y
    size = 40  # Half-size of shape for center alignment

    if shape == "Rectangle":
        canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=color)
    elif shape == "Oval":
        canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)

# Root window
root = tk.Tk()
root.title("Canvas Drawing Shapes Tool")
root.geometry("500x500")

# Shape selection
shape_var = tk.StringVar()
shape_combo = ttk.Combobox(root, textvariable=shape_var, state="readonly")
shape_combo['values'] = ("Rectangle", "Oval")
shape_combo.current(0)
shape_combo.pack(pady=5)

# Color selection
color_var = tk.StringVar()
color_combo = ttk.Combobox(root, textvariable=color_var, state="readonly")
color_combo['values'] = ("red", "green", "blue", "yellow", "black", "orange")
color_combo.current(0)
color_combo.pack(pady=5)

# Canvas widget
canvas = tk.Canvas(root, bg="white", width=450, height=400)
canvas.pack(padx=10, pady=10)
canvas.bind("<Button-1>", draw_shape)

root.mainloop()
