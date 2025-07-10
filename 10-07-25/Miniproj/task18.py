import tkinter as tk
import threading
import time
from datetime import datetime

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

class SystemInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Info Viewer")
        self.root.geometry("350x200")

        self.label = tk.Label(root, text="Press Start to Monitor", font=("Arial", 16))
        self.label.pack(pady=30)

        self.start_btn = tk.Button(root, text="Start Monitoring", command=self.start_monitoring)
        self.start_btn.pack(side=tk.LEFT, padx=20, pady=20)

        self.stop_btn = tk.Button(root, text="Stop", command=self.stop_monitoring, state='disabled')
        self.stop_btn.pack(side=tk.RIGHT, padx=20, pady=20)

        self.running = False
        self.thread = None

    def start_monitoring(self):
        if not self.running:
            self.running = True
            self.start_btn.config(state='disabled')
            self.stop_btn.config(state='normal')
            self.thread = threading.Thread(target=self.monitor_loop, daemon=True)
            self.thread.start()

    def stop_monitoring(self):
        self.running = False
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')

    def monitor_loop(self):
        while self.running:
            if PSUTIL_AVAILABLE:
                info = f"CPU Usage: {psutil.cpu_percent()}%"
            else:
                info = "Time: " + datetime.now().strftime("%H:%M:%S")
            self.root.after(0, self.update_label, info)
            time.sleep(1)

    def update_label(self, text):
        self.label.config(text=text)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SystemInfoApp(root)
    root.mainloop()
