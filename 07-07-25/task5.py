import tkinter as tk
from tkinter import messagebox

class AnimatedMover:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Object Mover")
        self.root.geometry("500x300")
        
        # Canvas setup
        self.canvas = tk.Canvas(root, width=400, height=150, bg="lightblue")
        self.canvas.pack(pady=10)

        # Create a rectangle
        self.rect = self.canvas.create_rectangle(10, 60, 60, 110, fill="green")

        # Speed Spinbox
        speed_frame = tk.Frame(root)
        speed_frame.pack(pady=5)

        tk.Label(speed_frame, text="Speed (ms):").pack(side=tk.LEFT)
        self.speed_var = tk.StringVar(value="100")
        self.speed_spinbox = tk.Spinbox(speed_frame, from_=10, to=1000, increment=10, textvariable=self.speed_var, width=5)
        self.speed_spinbox.pack(side=tk.LEFT)

        # Start / Stop Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="Start", width=10, command=self.start_animation)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", width=10, command=self.stop_animation, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=5)

        # Animation state
        self.animating = False

    def validate_speed(self):
        try:
            speed = int(self.speed_var.get())
            if speed < 10 or speed > 1000:
                raise ValueError
            return speed
        except ValueError:
            messagebox.showerror("Invalid Speed", "Please enter a valid number between 10 and 1000.")
            return None

    def move_rectangle(self):
        if self.animating:
            self.canvas.move(self.rect, 5, 0)
            x1, _, x2, _ = self.canvas.coords(self.rect)

            # Wrap around if it goes off screen
            if x2 > 400:
                self.canvas.move(self.rect, -x2, 0)

            speed = self.validate_speed()
            if speed:
                self.root.after(speed, self.move_rectangle)

    def start_animation(self):
        speed = self.validate_speed()
        if speed is not None:
            self.animating = True
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            self.move_rectangle()

    def stop_animation(self):
        self.animating = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedMover(root)
    root.mainloop()
