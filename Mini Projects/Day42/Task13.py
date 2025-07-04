import tkinter as tk
from tkinter import messagebox
import time
import winsound  # For Windows beep

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Countdown Timer")

        # Variables
        self.total_time = 0
        self.remaining_time = 0
        self.running = False
        self.paused = False

        # Spinbox to set time
        tk.Label(root, text="Seconds:").pack()
        self.time_spin = tk.Spinbox(root, from_=1, to=3600, width=10)
        self.time_spin.pack(pady=5)
        self.time_spin.delete(0, tk.END)
        self.time_spin.insert(0, "10")

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start_timer)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        self.pause_btn = tk.Button(btn_frame, text="Pause", state='disabled', command=self.pause_timer)
        self.pause_btn.pack(side=tk.LEFT, padx=5)
        self.resume_btn = tk.Button(btn_frame, text="Resume", state='disabled', command=self.resume_timer)
        self.resume_btn.pack(side=tk.LEFT, padx=5)

        # Canvas for animation
        self.canvas = tk.Canvas(root, width=200, height=200, bg="white")
        self.canvas.pack(pady=10)
        self.arc = self.canvas.create_arc(10, 10, 190, 190, start=90, extent=360, fill="skyblue")

        # Text timer on canvas
        self.timer_text = self.canvas.create_text(100, 100, text="", font=("Arial", 20), fill="black")

    def start_timer(self):
        try:
            self.total_time = int(self.time_spin.get())
            self.remaining_time = self.total_time
            self.running = True
            self.paused = False
            self.update_canvas()
            self.countdown()
            self.start_btn.config(state='disabled')
            self.pause_btn.config(state='normal')
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of seconds.")

    def pause_timer(self):
        self.paused = True
        self.pause_btn.config(state='disabled')
        self.resume_btn.config(state='normal')

    def resume_timer(self):
        self.paused = False
        self.countdown()
        self.pause_btn.config(state='normal')
        self.resume_btn.config(state='disabled')

    def countdown(self):
        if self.running and not self.paused:
            if self.remaining_time > 0:
                self.update_canvas()
                self.remaining_time -= 1
                self.root.after(1000, self.countdown)
            else:
                self.running = False
                self.update_canvas(final=True)
                self.start_btn.config(state='normal')
                self.pause_btn.config(state='disabled')
                self.resume_btn.config(state='disabled')
                winsound.Beep(1000, 500)  # Sound alert (Windows only)
                messagebox.showinfo("Time's up!", "Countdown completed.")

    def update_canvas(self, final=False):
        extent = (self.remaining_time / self.total_time) * 360 if self.total_time else 0
        self.canvas.itemconfig(self.arc, extent=extent)
        time_text = f"{self.remaining_time}s" if not final else "0s"
        self.canvas.itemconfig(self.timer_text, text=time_text)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
