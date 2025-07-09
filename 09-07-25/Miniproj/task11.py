import tkinter as tk

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer with Start/Stop/Reset")
        self.master.geometry("300x200")
        
        self.time_elapsed = 0  # in seconds
        self.running = False
        self.timer_id = None

        # Timer Label
        self.label = tk.Label(master, text="00:00:00", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # Buttons
        self.start_btn = tk.Button(master, text="Start", command=self.start_timer)
        self.start_btn.pack(side="left", padx=10, pady=20)

        self.stop_btn = tk.Button(master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_btn.pack(side="left", padx=10)

        self.reset_btn = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_btn.pack(side="left", padx=10)

    def format_time(self):
        h = self.time_elapsed // 3600
        m = (self.time_elapsed % 3600) // 60
        s = self.time_elapsed % 60
        return f"{h:02}:{m:02}:{s:02}"

    def update_timer(self):
        if self.running:
            self.time_elapsed += 1
            self.label.config(text=self.format_time())
            self.timer_id = self.master.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")

    def stop_timer(self):
        if self.running:
            self.running = False
            if self.timer_id:
                self.master.after_cancel(self.timer_id)
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")

    def reset_timer(self):
        self.stop_timer()
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
