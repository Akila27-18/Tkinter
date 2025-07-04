import tkinter as tk
from tkinter import ttk

# Function to update coordinates and draw shape
def draw_shape(event, shape_type):
    x, y = event.x, event.y
    label_coords.config(text=f"Clicked at: ({x}, {y})")
    color = combo_color.get()

    if shape_type == "circle":
        canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="")
    elif shape_type == "square":
        canvas.create_rectangle(x-20, y-20, x+20, y+20, fill=color, outline="")

# Wrapper for left-click (circle)
def left_click(event):
    draw_shape(event, "circle")

# Wrapper for right-click (square)
def right_click(event):
    draw_shape(event, "square")

# --- GUI setup
root = tk.Tk()
root.title("Shape Drawing with Coordinates")
root.geometry("500x500")

# Top Frame for color selection and coordinate display
frame_top = tk.Frame(root, pady=10)
frame_top.pack()

tk.Label(frame_top, text="Select Color:").pack(side=tk.LEFT, padx=5)

combo_color = ttk.Combobox(frame_top, values=["red", "blue", "green", "orange", "purple", "black"], state="readonly")
combo_color.set("black")
combo_color.pack(side=tk.LEFT, padx=5)

label_coords = tk.Label(frame_top, text="Clicked at: ( , )")
label_coords.pack(side=tk.LEFT, padx=20)

# Canvas for drawing
canvas = tk.Canvas(root, bg="white", width=480, height=400)
canvas.pack(padx=10, pady=10)

# Bind mouse events
canvas.bind("<Button-1>", left_click)   # Left click
canvas.bind("<Button-3>", right_click)  # Right click

root.mainloop()
