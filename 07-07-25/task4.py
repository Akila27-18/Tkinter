import tkinter as tk
from tkinter import ttk, messagebox

def on_canvas_click(event):
    shape = shape_var.get()
    x, y = event.x, event.y
    coord_label.config(text=f"Clicked at: ({x}, {y})")

    if shape == "":
        messagebox.showwarning("Selection Required", "Please select a shape.")
        return

    size = 50  # default size for shapes

    if shape == "Circle":
        canvas.create_oval(x - size, y - size, x + size, y + size, fill="skyblue", outline="blue")
    elif shape == "Rectangle":
        canvas.create_rectangle(x - size, y - size, x + size, y + size, fill="lightgreen", outline="green")
    elif shape == "Line":
        canvas.create_line(x - size, y - size, x + size, y + size, fill="black", width=2)

# Main window
root = tk.Tk()
root.title("Shape Drawing Canvas")
root.geometry("500x500")

# Shape selector
shape_var = tk.StringVar()
ttk.Label(root, text="Select Shape:").pack(pady=5)
shape_combo = ttk.Combobox(root, textvariable=shape_var, state="readonly")
shape_combo['values'] = ("Circle", "Rectangle", "Line")
shape_combo.pack(pady=5)

# Canvas
canvas = tk.Canvas(root, bg="white", width=400, height=350, relief="ridge", borderwidth=2)
canvas.pack(pady=10)
canvas.bind("<Button-1>", on_canvas_click)

# Coordinate display
coord_label = ttk.Label(root, text="Click on canvas to draw")
coord_label.pack(pady=5)

# Run app
root.mainloop()
