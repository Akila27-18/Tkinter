import tkinter as tk
from tkinter import ttk

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer with Canvas")
        self.root.geometry("350x300")

        # Variables
        self.total_time = 0
        self.remaining_time = 0
        self.running = False
        self.timer_id = None

        # Duration Spinbox
        ttk.Label(root, text="Set Duration (seconds):").pack(pady=5)
        self.time_spin = tk.Spinbox(root, from_=5, to=300, width=10)
        self.time_spin.pack()

        # Time display
        self.time_label = ttk.Label(root, text="Time Remaining: 0", font=("Arial", 14))
        self.time_label.pack(pady=10)

        # Canvas for animation
        self.canvas = tk.Canvas(root, width=300, height=30, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(pady=20)
        self.bar = self.canvas.create_rectangle(0, 0, 300, 30, fill="skyblue")

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Start", command=self.start_timer).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Pause", command=self.pause_timer).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Reset", command=self.reset_timer).grid(row=0, column=2, padx=5)

    def start_timer(self):
        if not self.running:
            self.total_time = int(self.time_spin.get())
            self.remaining_time = self.total_time if self.remaining_time == 0 else self.remaining_time
            self.running = True
            self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            self.time_label.config(text=f"Time Remaining: {self.remaining_time}s")

            # Update canvas bar width
            width = (self.remaining_time / self.total_time) * 300
            self.canvas.coords(self.bar, 0, 0, width, 30)

            self.remaining_time -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.time_label.config(text="Time's up!")
            self.running = False
            self.canvas.coords(self.bar, 0, 0, 0, 30)

    def pause_timer(self):
        if self.running:
            self.root.after_cancel(self.timer_id)
            self.running = False

    def reset_timer(self):
        if self.running:
            self.root.after_cancel(self.timer_id)
        self.running = False
        self.remaining_time = 0
        self.time_label.config(text="Time Remaining: 0")
        self.canvas.coords(self.bar, 0, 0, 300, 30)

# Run app
root = tk.Tk()
app = CountdownTimer(root)
root.mainloop()
