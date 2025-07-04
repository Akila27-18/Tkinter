import tkinter as tk

class AnimationPlayground:
    def __init__(self, root):
        self.root = root
        self.root.title("Animation Playground")

        # Canvas
        self.canvas = tk.Canvas(root, width=600, height=300, bg="white")
        self.canvas.pack(pady=10)

        # Draw rectangle
        self.rect = self.canvas.create_rectangle(10, 100, 60, 150, fill="skyblue")

        # Speed control
        control_frame = tk.Frame(root)
        control_frame.pack(pady=5)

        tk.Label(control_frame, text="Speed (ms delay):").grid(row=0, column=0, padx=5)
        self.speed_spin = tk.Spinbox(control_frame, from_=1, to=100, width=5)
        self.speed_spin.grid(row=0, column=1, padx=5)
        self.speed_spin.delete(0, tk.END)
        self.speed_spin.insert(0, "20")

        # Pause/Resume buttons
        self.pause_btn = tk.Button(control_frame, text="Pause", command=self.pause_animation)
        self.pause_btn.grid(row=0, column=2, padx=10)

        self.resume_btn = tk.Button(control_frame, text="Resume", command=self.resume_animation)
        self.resume_btn.grid(row=0, column=3, padx=10)

        # Coordinates label
        self.coord_label = tk.Label(root, text="X: 10, Y: 100")
        self.coord_label.pack()

        # Animation flags
        self.paused = False
        self.animate()

    def animate(self):
        if not self.paused:
            self.canvas.move(self.rect, 5, 0)
            coords = self.canvas.coords(self.rect)
            if coords[2] >= self.canvas.winfo_width():  # Reset if it goes out of bounds
                self.canvas.coords(self.rect, 0, 100, 50, 150)
                coords = self.canvas.coords(self.rect)

            self.coord_label.config(text=f"X: {int(coords[0])}, Y: {int(coords[1])}")

        delay = int(self.speed_spin.get())
        self.root.after(delay, self.animate)

    def pause_animation(self):
        self.paused = True

    def resume_animation(self):
        self.paused = False

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AnimationPlayground(root)
    root.mainloop()
