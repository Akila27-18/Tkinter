import tkinter as tk

class ShapeAnimator:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Animation Simulator")
        self.root.geometry("600x300")

        # --- Frames ---
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(pady=10)

        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        # --- Canvas ---
        self.canvas = tk.Canvas(self.canvas_frame, width=500, height=150, bg="white")
        self.canvas.pack()
        self.rect = self.canvas.create_rectangle(10, 60, 60, 110, fill="blue")

        # --- Controls ---
        tk.Label(self.control_frame, text="Speed (px):").grid(row=0, column=0, padx=5)
        self.speed_spinbox = tk.Spinbox(self.control_frame, from_=1, to=20, width=5)
        self.speed_spinbox.grid(row=0, column=1, padx=5)
        self.speed_spinbox.delete(0, tk.END)
        self.speed_spinbox.insert(0, "5")

        self.start_btn = tk.Button(self.control_frame, text="Start", command=self.start_animation)
        self.start_btn.grid(row=0, column=2, padx=5)

        self.pause_btn = tk.Button(self.control_frame, text="Pause", command=self.pause_animation)
        self.pause_btn.grid(row=0, column=3, padx=5)

        self.reset_btn = tk.Button(self.control_frame, text="Reset", command=self.reset_animation)
        self.reset_btn.grid(row=0, column=4, padx=5)

        # --- Animation Variables ---
        self.running = False
        self.animation_id = None

    def animate(self):
        if not self.running:
            return
        speed = int(self.speed_spinbox.get())
        self.canvas.move(self.rect, speed, 0)
        x1, y1, x2, y2 = self.canvas.coords(self.rect)

        if x2 >= self.canvas.winfo_width():
            self.running = False
            return

        self.animation_id = self.canvas.after(50, self.animate)

    def start_animation(self):
        if not self.running:
            self.running = True
            self.animate()

    def pause_animation(self):
        self.running = False
        if self.animation_id:
            self.canvas.after_cancel(self.animation_id)

    def reset_animation(self):
        self.pause_animation()
        self.canvas.coords(self.rect, 10, 60, 60, 110)

# --- Run App ---
root = tk.Tk()
app = ShapeAnimator(root)
root.mainloop()
