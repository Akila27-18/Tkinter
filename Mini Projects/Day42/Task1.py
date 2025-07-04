import tkinter as tk
from tkinter import ttk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Tool Application")

        # Canvas
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(pady=10)

        # Controls Frame
        control_frame = tk.Frame(root)
        control_frame.pack()

        # Shape Selector
        tk.Label(control_frame, text="Shape:").grid(row=0, column=0, padx=5)
        self.shape_var = tk.StringVar()
        self.shape_cb = ttk.Combobox(control_frame, textvariable=self.shape_var, values=["Rectangle", "Circle", "Line"], state="readonly")
        self.shape_cb.grid(row=0, column=1, padx=5)
        self.shape_cb.set("Rectangle")

        # Color Selector
        tk.Label(control_frame, text="Color:").grid(row=0, column=2, padx=5)
        self.color_var = tk.StringVar()
        self.color_cb = ttk.Combobox(control_frame, textvariable=self.color_var, values=["Red", "Green", "Blue", "Black"], state="readonly")
        self.color_cb.grid(row=0, column=3, padx=5)
        self.color_cb.set("Black")

        # Thickness Selector
        tk.Label(control_frame, text="Thickness:").grid(row=0, column=4, padx=5)
        self.size_spin = tk.Spinbox(control_frame, from_=1, to=10, width=5)
        self.size_spin.grid(row=0, column=5, padx=5)

        # Clear Button
        clear_btn = tk.Button(control_frame, text="Clear Canvas", command=self.clear_canvas)
        clear_btn.grid(row=0, column=6, padx=10)

        # Canvas click
        self.canvas.bind("<Button-1>", self.draw_shape)

    def draw_shape(self, event):
        shape = self.shape_var.get()
        color = self.color_var.get().lower()
        thickness = int(self.size_spin.get())

        x, y = event.x, event.y
        size = 40  # default shape size

        if shape == "Rectangle":
            self.canvas.create_rectangle(x, y, x + size, y + size, outline=color, width=thickness)
        elif shape == "Circle":
            self.canvas.create_oval(x, y, x + size, y + size, outline=color, width=thickness)
        elif shape == "Line":
            self.canvas.create_line(x, y, x + size, y + size, fill=color, width=thickness)

    def clear_canvas(self):
        self.canvas.delete("all")

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
