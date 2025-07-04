import tkinter as tk
from tkinter import ttk

# Helper function to draw a star
def draw_star(canvas, x, y, size=20, color="gold"):
    r = size
    points = [
        x, y - r,
        x + 0.2245 * r, y - 0.309 * r,
        x + r, y - 0.309 * r,
        x + 0.363 * r, y + 0.118 * r,
        x + 0.588 * r, y + 0.809 * r,
        x, y + 0.382 * r,
        x - 0.588 * r, y + 0.809 * r,
        x - 0.363 * r, y + 0.118 * r,
        x - r, y - 0.309 * r,
        x - 0.2245 * r, y - 0.309 * r
    ]
    return canvas.create_polygon(points, fill=color, outline="black")

# Main App
root = tk.Tk()
root.title("Simple Drawing Game")

# Shape selection
shape_var = tk.StringVar(value="star")
shapes = ["star", "ball", "square"]
shape_combo = ttk.Combobox(root, textvariable=shape_var, values=shapes, state="readonly")
shape_combo.pack(pady=5)

# Canvas setup
canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack(padx=10, pady=5)

# Listbox with scrollbar
frame_log = tk.Frame(root)
frame_log.pack(pady=5)

scrollbar = tk.Scrollbar(frame_log)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_listbox = tk.Listbox(frame_log, height=10, yscrollcommand=scrollbar.set, width=40)
log_listbox.pack()

scrollbar.config(command=log_listbox.yview)

# History to track drawn shapes
drawn_items = []

# Draw handler
def draw_shape(event):
    shape = shape_var.get()
    x, y = event.x, event.y

    if shape == "star":
        item = draw_star(canvas, x, y)
    elif shape == "ball":
        item = canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="skyblue", outline="black")
    elif shape == "square":
        item = canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill="salmon", outline="black")
    
    drawn_items.append(item)
    log_listbox.insert(tk.END, f"{shape.title()} at ({x}, {y})")

# Undo functionality
def undo_last():
    if drawn_items:
        last = drawn_items.pop()
        canvas.delete(last)
        log_listbox.delete(tk.END)

# Bind canvas click
canvas.bind("<Button-1>", draw_shape)

# Undo Button
undo_btn = tk.Button(root, text="Undo", command=undo_last)
undo_btn.pack(pady=5)

root.mainloop()
