import tkinter as tk

def update_canvas_size():
    w = int(width_spin.get())
    h = int(height_spin.get())
    canvas.config(width=w, height=h)

root = tk.Tk()
root.title("Canvas Size Controller")

# Spinbox for width
tk.Label(root, text="Width:").pack()
width_spin = tk.Spinbox(root, from_=100, to=800, increment=50, command=update_canvas_size)
width_spin.pack()

# Spinbox for height
tk.Label(root, text="Height:").pack()
height_spin = tk.Spinbox(root, from_=100, to=600, increment=50, command=update_canvas_size)
height_spin.pack()

# Canvas
canvas = tk.Canvas(root, bg="lightblue", width=300, height=200)
canvas.pack(pady=10)

# Set default values
width_spin.delete(0, tk.END)
width_spin.insert(0, "300")

height_spin.delete(0, tk.END)
height_spin.insert(0, "200")

root.mainloop()
