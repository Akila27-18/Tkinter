import tkinter as tk
from tkinter import ttk
import random

class ShapeAnimationEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Animation Editor")

        # Canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Controls Frame
        control_frame = tk.Frame(root)
        control_frame.pack()

        # Shape Combobox
        tk.Label(control_frame, text="Shape:").grid(row=0, column=0, padx=5)
        self.shape_var = tk.StringVar()
        shape_cb = ttk.Combobox(control_frame, textvariable=self.shape_var,
                                values=["Rectangle", "Circle"], state="readonly", width=10)
        shape_cb.grid(row=0, column=1)
        shape_cb.set("Rectangle")

        # Direction Combobox
        tk.Label(control_frame, text="Direction:").grid(row=0, column=2, padx=5)
        self.direction_var = tk.StringVar()
        dir_cb = ttk.Combobox(control_frame, textvariable=self.direction_var,
                              values=["Right", "Left", "Up", "Down"], state="readonly", width=10)
        dir_cb.grid(row=0, column=3)
        dir_cb.set("Right")

        # Speed Spinbox
        tk.Label(control_frame, text="Speed (ms):").grid(row=0, column=4, padx=5)
        self.speed_spin = tk.Spinbox(control_frame, from_=10, to=1000, width=6)
        self.speed_spin.grid(row=0, column=5)
        self.speed_spin.delete(0, tk.END)
        self.speed_spin.insert(0, "30")

        # Add Shape Button
        add_btn = tk.Button(control_frame, text="Add Shape", command=self.add_shape)
        add_btn.grid(row=0, column=6, padx=10)

        # Pause/Stop Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Pause All", command=self.pause_all).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Resume All", command=self.resume_all).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Stop All", command=self.stop_all).pack(side=tk.LEFT, padx=5)

        # Track shapes and flags
        self.shapes = []  # List of dicts {id, dx, dy, speed, paused, stopped}

    def add_shape(self):
        shape_type = self.shape_var.get()
        direction = self.direction_var.get()
        speed = int(self.speed_spin.get())

        # Random start position
        x = random.randint(50, 550)
        y = random.randint(50, 350)
        size = 30

        # Create shape
        if shape_type == "Rectangle":
            shape_id = self.canvas.create_rectangle(x, y, x+size, y+size, fill="skyblue")
        elif shape_type == "Circle":
            shape_id = self.canvas.create_oval(x, y, x+size, y+size, fill="orange")

        # Determine movement delta
        dx, dy = 0, 0
        if direction == "Right":
            dx = 5
        elif direction == "Left":
            dx = -5
        elif direction == "Up":
            dy = -5
        elif direction == "Down":
            dy = 5

        shape_info = {
            "id": shape_id,
            "dx": dx,
            "dy": dy,
            "speed": speed,
            "paused": False,
            "stopped": False
        }

        self.shapes.append(shape_info)
        self.animate(shape_info)

    def animate(self, shape_info):
        if shape_info["stopped"]:
            return
        if not shape_info["paused"]:
            self.canvas.move(shape_info["id"], shape_info["dx"], shape_info["dy"])
            self.keep_in_bounds(shape_info["id"])

        self.root.after(shape_info["speed"], lambda: self.animate(shape_info))

    def keep_in_bounds(self, shape_id):
        x1, y1, x2, y2 = self.canvas.coords(shape_id)
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if x1 < 0 or x2 > w:
            self.canvas.move(shape_id, -5 if x1 < 0 else -5, 0)
        if y1 < 0 or y2 > h:
            self.canvas.move(shape_id, 0, -5 if y1 < 0 else -5)

    def pause_all(self):
        for shape in self.shapes:
            shape["paused"] = True

    def resume_all(self):
        for shape in self.shapes:
            if not shape["stopped"]:
                shape["paused"] = False

    def stop_all(self):
        for shape in self.shapes:
            shape["stopped"] = True

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeAnimationEditor(root)
    root.mainloop()
