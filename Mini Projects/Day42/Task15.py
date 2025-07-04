import tkinter as tk

class FitnessRepetitionCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Repetition Counter")

        self.reps_total = 0
        self.current_rep = 0
        self.running = False

        tk.Label(root, text="Set Reps:").pack()
        self.reps_spin = tk.Spinbox(root, from_=1, to=100, width=5)
        self.reps_spin.pack(pady=5)
        self.reps_spin.delete(0, tk.END)
        self.reps_spin.insert(0, "10")

        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)

        self.btn = tk.Button(root, text="Start", command=self.toggle_animation)
        self.btn.pack()

        self.parts = {}
        self.draw_figure(y_offset=0)

    def draw_figure(self, y_offset):
        self.canvas.delete("all")
        center_x = 150
        head_r = 15
        body_len = 40

        self.parts['head'] = self.canvas.create_oval(
            center_x - head_r, 50 + y_offset - head_r,
            center_x + head_r, 50 + y_offset + head_r,
            fill="lightblue"
        )

        self.parts['body'] = self.canvas.create_line(
            center_x, 50 + y_offset + head_r,
            center_x, 50 + y_offset + head_r + body_len,
            width=3
        )

        self.parts['arms'] = self.canvas.create_line(
            center_x - 20, 50 + y_offset + head_r + 10,
            center_x + 20, 50 + y_offset + head_r + 10,
            width=3
        )

        self.parts['left_leg'] = self.canvas.create_line(
            center_x, 50 + y_offset + head_r + body_len,
            center_x - 20, 50 + y_offset + head_r + body_len + 30,
            width=3
        )

        self.parts['right_leg'] = self.canvas.create_line(
            center_x, 50 + y_offset + head_r + body_len,
            center_x + 20, 50 + y_offset + head_r + body_len + 30,
            width=3
        )

        self.canvas.create_text(150, 20, text=f"Rep: {self.current_rep}/{self.reps_total}", font=("Arial", 14))

    def toggle_animation(self):
        if not self.running:
            self.reps_total = int(self.reps_spin.get())
            self.current_rep = 0
            self.running = True
            self.btn.config(text="Stop")
            self.animate()
        else:
            self.running = False
            self.btn.config(text="Start")

    def animate(self):
        if not self.running:
            return

        self.draw_figure(y_offset=-20)
        self.root.after(200, self.animate_down)

    def animate_down(self):
        if not self.running:
            return

        self.current_rep += 1  # ✅ Increment first!
        self.draw_figure(y_offset=0)

        if self.current_rep >= self.reps_total:
            self.running = False
            self.btn.config(text="Start")
        else:
            self.root.after(400, self.animate)

# Run it
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessRepetitionCounter(root)
    root.mainloop()
